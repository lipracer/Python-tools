
#include <iostream>
#include <vector>
#include <chrono>
#include <thread>
#include <string>
#include <list>

using namespace std;
using namespace chrono;

/*
huawei question:
example aBBbb123aca
output:
a=3
B=2
b=2
c=1
������Ȱ����ȳ����ȴ�ӡ
*/

struct char_info
{
	int count;
	int first_appear_index;
	char value;
	char_info() : count(0), first_appear_index(-1) {}
};
void computer_count(const string& str);

void print_mitrax