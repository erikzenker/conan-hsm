# Conan Hsm Package

Run the following commands to create and upload the hsm package 
```bash
conan create . erikzenker/testing -s compiler.cppstd=17
conan remote add conan-erikzenker https://api.bintray.com/conan/erikzenker/conan-erikzenker
conan user -p <APIKEY> -r conan-erikzenker erikzenker
conan upload hsm/1.1 -r conan-erikzenker
```

The API key is the “password” used to authenticate the Conan client to Bintray, NOT your Bintray password. To get your API key, go to “Edit Your Profile” in your Bintray account and check the API Key section.