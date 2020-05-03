# When do I need this?
If you never want to create super nested loop, maybe never you will need this.  
Just for sometimes you want to create super nested loop like this.
```
for (int i1 = 1; i1 <= m; ++i1)
    {
        for (int i2 = i1; i2 <= m; ++i2)
        {
            for (int i3 = i2; i3 <= m; ++i3)
            {
                for (int i4 = i3; i4 <= m; ++i4)
                {
                    for (int i5 = i4; i5 <= m; ++i5)
                    {
                        for (int i6 = i5; i6 <= m; ++i6)
                        {
                            for (int i7 = i6; i7 <= m; ++i7)
                            {
                                for (int i8 = i7; i8 <= m; ++i8)
                                {
                                    for (int i9 = i8; i9 <= m; ++i9)
                                    {
                                        for (int i10 = i9; i10 <= m; ++i10)
                                        {
                                            //do something
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
```
But to be honest, you could write code like ...
```
int dfs(int i1, int i2, int i3, int i4, int i5, int i6, int i7, int i8, int i9, int i10)
{
    //do something
}
```
or
```
int dfs(const vector<int>& v)
{
    //do something
}
```

# Usage
python multi_loop.py \<loop num> \<loop initializer type> \<cond> \<loop statement type>  
### example:
python multi_loop.py 10 i '<= n' i
