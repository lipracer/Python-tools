//
//  main.cpp
//  solution
//
//  Created by ³ÂÁú on 2019/8/18.
//  Copyright ? 2019 ³ÂÁú. All rights reserved.
//

#include "solution.h"

//¼ÆÊýÅÅÐò
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

void computer_count(const string& str)
{
    char_info info[256];
    for (int i = 0; i < str.length(); i++)
    {
		int index = (int)str[i];
		if (0 == info[index].count)
		{
			info[index].first_appear_index = i;
		}
        info[index].count++;
		info[index].value = str[i];
    }
	list<char_info> mlist;
	for (int i = 0; i < 256; ++i) 
	{
		if (info[i].count) 
		{
			auto begin = mlist.begin();
			while (begin != mlist.end())
			{
				if (begin->count < info[i].count) 
				{
					break;
				}
				else if(begin->count == info[i].count) 
				{
					if (str.find(info[i].value) > begin->first_appear_index) 
					{
						begin++;
					}
					else 
					{
						break;
					}
				}
				else 
				{
					begin++;
				}
			}
			mlist.insert(begin, info[i]);
		}
	}
	for (auto it : mlist)
	{
		cout << it.value << "=" << it.count << endl;
	}
}