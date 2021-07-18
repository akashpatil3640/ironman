ACES-2K21 Technical Event
Round 2
Sunday, July 18, 2021

Problem Statement:

You are driving on highway, and see a tunnel having height 18 ft (H_T) and width 10ft (W_T), a container passes by your side having its length (L_C), height (H_C) and width (W_C) marked on it, you need to check whether that container will pass through the tunnel or not with its height and width and display result.
Also calculate volume of container only if container passes tunnel.
Check if volume of container is perfect square or not.

Constraints:<br>
0  < N <br>
0  <  L_C <  50 <br>
0  <  H_C <  30 <br>
0  <  W_C <  30<br>

Input:
The first line contains integer N (number of container to pass) 
Next N lines contains 3 integers each separated by single space, and which are length, height and, width in feet of the container.

Output Format:
First line of output contains PASS / FAIL denoting passing of container or not resp.
Second line contains an integer denoting volume of container only if container passes tunnel.
Third line displays if volume is perfect square or not as TRUE/FALSE, only if container passes tunnel.
/*(one blank line)*/
Repeat this output for N containers.

Sample Input:<br>
2<br>
40 12 8<br>
40 18 12<br>

Sample Output:
PASS<br>
3840<br>
FALSE<br>
<br><br>
FAIL<br>






Explanation:
N = 2<br>

For first container
Height and Width satisfy with given condition, As container passes shown its volume and checked for perfect square or not.

For the next container 
Width of container is greater than width of tunnel, so container cannot pass the tunnel hence displayed FAIL as result.

Run Code with this Input and Take Screenshots
3<br>
32 16 8<br>
40 12 8<br>
30 11 11<br>
