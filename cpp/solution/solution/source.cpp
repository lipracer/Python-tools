//
//  main.cpp
//  solution
//
//  Created by ³ÂÁú on 2019/8/18.
//  Copyright ? 2019 ³ÂÁú. All rights reserved.
//

#include <iostream>
#include <vector>
#include <chrono>
#include <thread>

using namespace std;
using namespace chrono;

template<size_t max_value>
void count_sort(size_t array[], size_t length, size_t out[])
{
    size_t *counts = new size_t[max_value];
    memset(counts, 0, sizeof(size_t) * max_value);
    
    for(size_t i  = 0; i < length; ++i)
    {
        counts[array[i]]++;
    }
    for (size_t i = 1; i < max_value; i++)
    {
        counts[i] = counts[i-1] + counts[i];
    }
    
    for (size_t i = 0; i < length; i++)
    {
        counts[array[i]]--;
        out[counts[array[i]]] = array[i];
    }
    
    delete [] counts;
}

struct char_info
{
    int count;
    int first_appear_index;
    char_info() : count(0), first_appear_index(-1){}
};

void computer_count(const string& str)
{
    char_info info[256];
    for (int i = 0; i < str.length(); i++)
    {
        if(0 == info[(int)str[i]].count) info[(int)str[i]].first_appear_index = i;
        info[(int)str[i]].count++;
    }
}

const size_t MaxTestValue = 256;
const size_t test_count = 100;

int main(int argc, const char * argv[])
{
    string target = "easbfjbaeognaerlkbn";
    computer_count(target);
    
    size_t arr[test_count] = { 0 };
    size_t out[test_count] = { 0 };
    
    for (size_t i = 0; i < test_count; i++)
    {
        arr[i] = rand() % MaxTestValue;
    }
    count_sort<MaxTestValue>(arr, test_count, out);
    
    return 0;
}
