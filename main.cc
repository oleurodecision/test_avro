#include <avro/DataFile.hh>

struct miam {};

int main()
{
	avro::DataFileReader<miam> dfr("not/a/valid/path");
}

