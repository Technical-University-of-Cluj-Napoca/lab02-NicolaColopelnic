import os
from datetime import datetime

def smart_log(*args, **kwargs) -> None:
    blue = "\033[34m"
    gray = "\033[90m"
    yellow = "\033[33m"
    red = "\033[31m"
    reset = "\033[0m"

    level = kwargs.get("level", "info").lower()
    timestamp = kwargs.get("timestamp", True)
    date = kwargs.get("date", False)
    color = kwargs.get("color", True)
    save_to = kwargs.get("save_to", None)

    if level == "info":
        level_color = blue
    elif level == "debug":
        level_color = gray
    elif level == "warning":
        level_color = yellow
    elif level == "error":
        level_color = red
    else:
        level_color = ""

    message = " ".join(str(part) for part in args)

    time_str = ""
    if date:
        time_str += datetime.now().strftime("%Y-%m-%d ")
    if timestamp:
        time_str += datetime.now().strftime("%H:%M:%S ")

    output = f"{time_str}[{level.upper()}] {message}"

    if color and level_color:
        output = level_color + output + reset

    print(output)

    if save_to:
        os.makedirs(os.path.dirname(save_to), exist_ok=True)
        with open(save_to, "a") as f:
            f.write(output + "\n")


smart_log("System started successfully.", level="info")
smart_log("User", "alice", "logged in", level="debug", timestamp=True)
smart_log("Low disk space detected!", level="warning", save_to="logs/system.log")
smart_log("Model", "training", "failed!", level="error", color = True, save_to="logs/errors.log")
smart_log("Process end", level="info", color=False, save_to="logs/errors.log")
