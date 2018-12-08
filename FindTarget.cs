using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace indices
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] nums = new int[5];
            nums[0] = 2;
            nums[1] = 7;
            nums[2] = 11;
            nums[3] = 15;
            nums[4] = 2;
            int target= 17;
            for (int i = 0; i < nums.Length -1; i++)
            {
                if (nums[i]+nums[i + 1]==target){
                    System.Console.WriteLine(i.ToString() + " "+ (i + 1).ToString());
                }
                 
            }
            System.Console.ReadLine();
        }
    }
}
