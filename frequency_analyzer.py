import operator
import sys

/*
     Copyright 2010 Jason Berlinsky

     Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
 
     http://www.apache.org/licenses/LICENSE-2.0
 
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/

filename = sys.argv[1]

f = open(filename)

str = ""

for line in f:
    str = str + line

s = set(str)

frequencies = []

# Get the frequencies. This takes O(U*M), where U = len(s) and M = len(str)
for char in s:
    count = 0
    for i in range(0,len(str)):
        if (char == str[i]):
            count += 1
    frequencies.append((char,count))

frequencies = sorted(frequencies,key=operator.itemgetter(1)) # Sort by the tuple value in ascending order

for tuple in frequencies:
    if tuple[0] == "\n":
        tupleChar = "\\n" # This breaks the output.
    else:
        tupleChar = tuple[0]
    print "'"+tupleChar+"' occurs with a frequency of %d" % tuple[1]
