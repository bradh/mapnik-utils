import compile, style
from compile import compile
from style import stylesheet_declarations

def load_map(map, input, dir=None, move_local_files=False):
    """
    """
    compile(input, dir, move_local_files).to_mapnik(map)
