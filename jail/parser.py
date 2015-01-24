import re

NO_MODE = 0
STRING_MODE = 1


def get_jails_config(filename='jail.conf'):
    cfg = None
    try:
        with open(filename, 'r') as f:
            cfg = _remove_comments(f.read())
    finally:
        return cfg


def _remove_comments(cfg):
    cfg_structure = ""
    curr_mode = NO_MODE
    curr_c = 0
    cfg_nb_c = len(cfg)
    while curr_c < cfg_nb_c:
        if curr_mode == NO_MODE:
            # inline comment
            if cfg[curr_c] == '#' or cfg[curr_c:curr_c+2] == "//":
                while cfg[curr_c] != '\n':
                    curr_c += 1
                curr_c += 1  # remove trailing newline character
            # multilines comment
            elif cfg[curr_c:curr_c+2] == "/*":
                while cfg[curr_c:curr_c+2] != "*/":
                    curr_c += 1
                curr_c += 2  # remove "*/" trailing characters
            # simple line / character
            else:
                # enter in string mode -> keep all characters
                if cfg[curr_c] == '"':
                    curr_mode = STRING_MODE

                cfg_structure += cfg[curr_c]
                curr_c += 1
        else:
            cfg_structure += cfg[curr_c]

            # quit string mode if it's a '"' character and if it's not escaped
            if cfg[curr_c] == '"' and cfg[curr_c-1] != '\\':
                curr_mode = NO_MODE

            curr_c += 1

    return cfg_structure
