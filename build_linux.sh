#!/bin/bash

build_dir=builds/linux
profile=gcc-10

rm -rf $build_dir
conan install . \
	-pr:b $profile -pr:h $profile \
	-s build_type=Release \
	-if $build_dir \
	-of $build_dir \
	--build outdated
conan build . -bf $build_dir
