from types import ModuleType
from pycreatedgml import AbstractModulesGraph
from example_files import module
from pathlib import Path


class ModulesGraph(AbstractModulesGraph):
    @classmethod
    def _to_show_module(cls, module: ModuleType) -> bool:
        return True
    
    @classmethod
    def _to_show_module_childs(cls, module: ModuleType) -> bool:
        try:
            Path(module.__file__).relative_to(Path(".").absolute() / Path("example_files")) # type: ignore
        except ValueError:
            return False
        else:
            return True
    


graph = ModulesGraph(module)


with open("graph.dgml", "w+") as f:
    f.write(graph.render())
