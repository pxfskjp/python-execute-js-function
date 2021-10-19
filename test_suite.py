import js2py
  
eval_res, tempfile = js2py.run_file("functions.js")
tempfile1 = tempfile.wish("GeeksforGeeks 1")
tempfile2 = tempfile.wish1("GeeksforGeeks 2")
tempfile3 = tempfile.wish2("GeeksforGeeks 3")
tempfile4 = tempfile.wish3("GeeksforGeeks 4")

print(tempfile1 ,tempfile2 ,tempfile3 ,tempfile4)