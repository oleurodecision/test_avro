set build_dir=builds\win
set profile=vs14

rmdir /S /Q %build_dir%

conan install . ^
	-pr:b %profile% -pr:h %profile% ^
	-c tools.microsoft.msbuild:verbosity=Diagnostic ^
	-s build_type=Release ^
	-if %build_dir% ^
	-of %build_dir% ^
	--build outdated 
conan build . -bf %build_dir%
