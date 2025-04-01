import time
import shutil

def ft_tqdm(lst: range) -> None:
    """Affiche une barre de chargement façon tqdm, avec yield."""
    total = len(lst)
    columns = shutil.get_terminal_size().columns
    start_time = time.time()

    for i in lst:
        percent = f"{((i + 1) / total * 100):.0f}" + "%"
        step = f"{i+1}/{total}"
        elapsed = time.time() - start_time
        speed = (i + 1) / elapsed if elapsed else 0
        time_remaining = (total - (i + 1)) / speed if speed else 0
        elapsed_str = time.strftime("%M:%S", time.gmtime(elapsed))
        remaining_str = time.strftime("%M:%S", time.gmtime(time_remaining))
        info = f"{step} [{(elapsed_str)}<{(remaining_str)}, {(speed):.2f}it/s]"

        bar_length = max(2, columns - (len(percent) + len(info)) - 3)

        filled_length = min(bar_length, int(bar_length * (i + 1) / total))
        bar = "█" * (filled_length) + " " * (bar_length - filled_length)

        line = f"\r{percent}|{bar}| {info}"
        if len(line) > columns + 3:
            line = line[:columns - 1]

        print(
            line,
            end="",
            flush=True
        )

        yield i