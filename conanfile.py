from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake

class TestAvro(ConanFile):
    settings = "os", "arch", "compiler", "build_type"

    def set_name(self):
        return "TestAvro"

    def set_version(self):
        return "0.0"
    
    def requirements(self):
        self.requires("libavrocpp/1.10.1@")

    def configure(self):
        if self.settings.compiler == "Visual Studio":
            self.options["boost"].magic_autolink = False
            self.options["boost"].without_url = True

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        
    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

        cd = CMakeDeps(self)
        cd.generate()

