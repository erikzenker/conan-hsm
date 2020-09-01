from conans import ConanFile, CMake, tools


class HsmConan(ConanFile):
    name = "hsm"
    version = "1.1"
    license = "MIT"
    author = "Erik Zenker erikzenker@hotmail.com"
    url = "https://github.com/erikzenker/hsm.git"
    description = "The hana state machine (hsm) is a finite state machine library based on the boost hana meta programming library. It follows the principles of the boost msm and boost sml libraries, but tries to reduce own complex meta programming code to a minimum."
    topics = ("state machine", "template meta programming")
    requires = "boost/1.72.0"
    no_copy_source = True
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/erikzenker/hsm.git")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="hsm/src")
        cmake.install()

    def package(self):
        self.copy("*.h", dst="include", src="hsm/src/include")
        self.copy("*.cmake", dst="lib/cmake/hsm", src="hsm/src/")

    def package_id(self):
        self.info.header_only()

    def package_info(self):
        self.info.header_only()
        self.cpp_info.libdirs = []
        self.cpp_info.libs = ["hsm"]

