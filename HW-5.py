class Indenter:
    space = None
    def __init__(self):
        self.value_multiply = -1
        
    def __enter__(self):
        self.value_multiply += 1
        return self

    def show(self, txt):
        Indenter.space = self.value_multiply * '    '
        print(f'{Indenter.space}{txt}')
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.value_multiply -= 1


with Indenter() as indent:
    indent.show('hi')
    with indent:
        indent.show('talk is cheap')
        with indent:
            indent.show('show me the code...')
    indent.show('torvalds')
    