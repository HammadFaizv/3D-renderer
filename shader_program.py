

class ShaderProgram:
    def __init__(self, ctx):
        self.ctx = ctx
        self.programs = {}
        self.programs['default'] = self.get_program('default')
        self.programs['skybox'] = self.get_program('skybox')

    def get_program(self, shader_name):
        with open(f'shaders/{shader_name}.vert') as f:
            vertex_shader = f.read()
        with open(f'shaders/{shader_name}.frag') as f:
            fragment_shader = f.read()

        return self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
    
    def destroy(self):
        [program.release() for program in self.programs.values()]