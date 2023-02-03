cmake_minimum_required (VERSION 3.23)

project (TestAvro
	VERSION 0.0
	LANGUAGES CXX)

find_package (libavrocpp REQUIRED)

add_executable (TestAvro)
target_sources (TestAvro
	PUBLIC
	main.cc)
target_link_libraries (TestAvro
	PUBLIC
	Boost::disable_autolinking
	libavrocpp::libavrocpp)

