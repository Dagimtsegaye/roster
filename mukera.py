from tkinter import Tk, Frame, Label, Entry, Button
from tkinter import ttk
import tkinter as tk


class App(Frame):
        def __init__(root, master):
            Frame.__init__(root, master)
            root.grid()
            root.create_widgets()

                      
                  
          # define the entry        
        def get_stu1(root):
          return [float(entry.get()) for entry in root.stu1M]            

        def get_stu2(root):
          return [float(entry.get()) for entry in root.stu2M] 
          
        def get_stu3(root):
          return [float(entry.get()) for entry in root.stu3M] 
          
        def get_stu4(root):
          return [float(entry.get()) for entry in root.stu4M]  
          
        def get_stu5(root):
          return [float(entry.get()) for entry in root.stu5M]   
        
        def get_stu6(root):
          return [float(entry.get()) for entry in root.stu6M]
          
        def get_stu7(root):
          return [float(entry.get()) for entry in root.stu7M]  
        
       
        def get_stu8(root):
          return [float(entry.get()) for entry in root.stu8M]       
       
        def get_stu9(root):
          return [float(entry.get()) for entry in root.stu9M]      
                
       
        def get_stu10(root):
          return [float(entry.get()) for entry in root.stu10M] 
        
        def ADD4(root):
            root.wb = openpyxl.Workbook()
            root.wb1 = openpyxl.Workbook()
            root.wb2 = openpyxl.Workbook()
            root.wb3 = openpyxl.Workbook()
            root.wb4 = openpyxl.Workbook()
            root.wb5 = openpyxl.Workbook()
            root.wb6 = openpyxl.Workbook()
            root.wb7 = openpyxl.Workbook()

            root.sheet = root.wb.active
            root.sheet1 = root.wb1.active
            root.sheet2 = root.wb2.active
            root.sheet3 = root.wb2.active
            root.sheet4 = root.wb4.active
            root.sheet5 = root.wb5.active
            root.sheet6 = root.wb6.active
            root.sheet7 = root.wb7.active

            #########################################################
            #merge_cells
            root.sheet1.merge_cells('A1:T3')
            root.sheet1.merge_cells('A26:T28')


            #Give_input
            root.sheet1.cell(row =4, column=1).value="No"
            root.sheet1.cell(row=4, column=2).value="Name"
            root.sheet1.cell(row=4, column=3).value="sex"
            root.sheet1.cell(row=4, column=4).value="Age"
            root.sheet1.cell(row=4, column=5).value="sem"
            root.sheet1.cell(row=4, column=6).value="AM"
            root.sheet1.cell(row=4, column=7).value="ENG"
            root.sheet1.cell(row=4, column=8).value="MA"
            root.sheet1.cell(row =4, column=9).value="PH"
            root.sheet1.cell(row=4, column=10).value="CH"
            root.sheet1.cell(row=4, column=11).value="BI"
            root.sheet1.cell(row=4, column=12).value="GI"
            root.sheet1.cell(row=4, column=13).value="HI"
            root.sheet1.cell(row=4, column=14).value="CV"
            root.sheet1.cell(row=4, column=15).value="HP"
            root.sheet1.cell(row=4, column=16).value="IT"
            root.sheet1.cell(row =4, column=17).value="SUM"
            root.sheet1.cell(row=4, column=18).value="AVRG"
            root.sheet1.cell(row=4, column=19).value="RANK"
            root.sheet1.cell(row=4, column=20).value="ATEND"
            root.sheet1.cell(row=4, column=21).value="COND"
            root.sheet1.cell(row=4, column=22).value="RMARK"


            root.sheet1.cell(row= 5, column=1).value= "1"
            root.sheet1.cell(row= 8, column=1).value= "2"
            root.sheet1.cell(row= 11, column=1).value= "3"
            root.sheet1.cell(row= 14, column=1).value= "4"
            root.sheet1.cell(row= 17, column=1).value= "5"
            root.sheet1.cell(row= 20, column=1).value= "6"
            root.sheet1.cell(row= 23, column=1).value= "7"
            root.sheet1.cell(row=5, column= 5).value = "1st"
            root.sheet1.cell(row=6, column= 5).value = "2nd"
            root.sheet1.cell(row=7, column= 5).value = "Avr"
            root.sheet1.cell(row=8, column= 5).value = "1st"
            root.sheet1.cell(row=9, column= 5).value = "2nd"
            root.sheet1.cell(row=10, column= 5).value = "Avr"
            root.sheet1.cell(row=11, column= 5).value = "1st"
            root.sheet1.cell(row=12, column= 5).value = "2nd"
            root.sheet1.cell(row=13, column= 5).value = "Avr"
            root.sheet1.cell(row=14, column= 5).value = "1st"
            root.sheet1.cell(row=15, column= 5).value = "2nd"
            root.sheet1.cell(row=16, column= 5).value = "Avr"
            root.sheet1.cell(row=17, column= 5).value = "1st"
            root.sheet1.cell(row=18, column= 5).value = "2nd"
            root.sheet1.cell(row=19, column= 5).value = "Avr"
            root.sheet1.cell(row=20, column= 5).value = "1st"
            root.sheet1.cell(row=21, column= 5).value = "2nd"
            root.sheet1.cell(row=22, column= 5).value = "Avr"
            root.sheet1.cell(row=23, column= 5).value = "1st"
            root.sheet1.cell(row=24, column= 5).value = "2nd"
            root.sheet1.cell(row=25, column= 5).value = "Avr"

            #merge_cells
            root.sheet1.merge_cells('A5:A7')
            root.sheet1.merge_cells('B5:B7')
            root.sheet1.merge_cells('C5:C7')
            root.sheet1.merge_cells('D5:D7')

            root.sheet1.merge_cells('A8:A10')
            root.sheet1.merge_cells('B8:B10')
            root.sheet1.merge_cells('C8:C10')
            root.sheet1.merge_cells('D8:D10')
            root.sheet1.merge_cells('D8:D10')

            root.sheet1.merge_cells('A11:A13')
            root.sheet1.merge_cells('B11:B13')
            root.sheet1.merge_cells('C11:C13')
            root.sheet1.merge_cells('D11:D13')
            root.sheet1.merge_cells('D11:D13')

            root.sheet1.merge_cells('A14:A16')
            root.sheet1.merge_cells('B14:B16')
            root.sheet1.merge_cells('C14:C16')
            root.sheet1.merge_cells('D14:D16')
            root.sheet1.merge_cells('D14:D16')

            root.sheet1.merge_cells('A17:A19')
            root.sheet1.merge_cells('B17:B19')
            root.sheet1.merge_cells('C17:C19')
            root.sheet1.merge_cells('D17:D19')
            root.sheet1.merge_cells('D17:D19')

            root.sheet1.merge_cells('A20:A22')
            root.sheet1.merge_cells('B20:B22')
            root.sheet1.merge_cells('C20:C22')
            root.sheet1.merge_cells('D20:D22')
            root.sheet1.merge_cells('D20:D22')

            root.sheet1.merge_cells('A23:A25')
            root.sheet1.merge_cells('B23:B25')
            root.sheet1.merge_cells('C23:C25')
            root.sheet1.merge_cells('D23:D25')
            root.sheet1.merge_cells('D23:D25')

            #column_dimensions
            root.sheet1.column_dimensions['B'].width= 25
            root.sheet1.column_dimensions['A'].width = 5
            root.sheet1.column_dimensions['C'].width = 5
            root.sheet1.column_dimensions['D'].width = 5
            
            
            # get the mark 
            
            
            

            root.wb1.save('8-14 students.xlsx')

            
            #########################################################
            #merge_cells
            root.sheet.merge_cells('A1:T3')
            root.sheet.merge_cells('A26:T28')


            #Give_input
            root.sheet.cell(row =4, column=1).value="No"
            root.sheet.cell(row=4, column=2).value="Name"
            root.sheet.cell(row=4, column=3).value="sex"
            root.sheet.cell(row=4, column=4).value="Age"
            root.sheet.cell(row=4, column=5).value="sem"
            root.sheet.cell(row=4, column=6).value="AM"
            root.sheet.cell(row=4, column=7).value="ENG"
            root.sheet.cell(row=4, column=8).value="MA"
            root.sheet.cell(row =4, column=9).value="PH"
            root.sheet.cell(row=4, column=10).value="CH"
            root.sheet.cell(row=4, column=11).value="BI"
            root.sheet.cell(row=4, column=12).value="GI"
            root.sheet.cell(row=4, column=13).value="HI"
            root.sheet.cell(row=4, column=14).value="CV"
            root.sheet.cell(row=4, column=15).value="HP"
            root.sheet.cell(row=4, column=16).value="IT"
            root.sheet.cell(row =4, column=17).value="SUM"
            root.sheet.cell(row=4, column=18).value="AVRG"
            root.sheet.cell(row=4, column=19).value="RANK"
            root.sheet.cell(row=4, column=20).value="ATEND"
            root.sheet.cell(row=4, column=21).value="COND"
            root.sheet.cell(row=4, column=22).value="RMARK"


            root.sheet.cell(row= 5, column=1).value= "8"
            root.sheet.cell(row= 8, column=1).value= "9"
            root.sheet.cell(row= 11, column=1).value= "10"
            root.sheet.cell(row= 14, column=1).value= "11"
            root.sheet.cell(row= 17, column=1).value= "12"
            root.sheet.cell(row= 20, column=1).value= "13"
            root.sheet.cell(row= 23, column=1).value= "14"
            root.sheet.cell(row=5, column= 5).value = "1st"
            root.sheet.cell(row=6, column= 5).value = "2nd"
            root.sheet.cell(row=7, column= 5).value = "Avr"
            root.sheet.cell(row=8, column= 5).value = "1st"
            root.sheet.cell(row=9, column= 5).value = "2nd"
            root.sheet.cell(row=10, column= 5).value = "Avr"
            root.sheet.cell(row=11, column= 5).value = "1st"
            root.sheet.cell(row=12, column= 5).value = "2nd"
            root.sheet.cell(row=13, column= 5).value = "Avr"
            root.sheet.cell(row=14, column= 5).value = "1st"
            root.sheet.cell(row=15, column= 5).value = "2nd"
            root.sheet.cell(row=16, column= 5).value = "Avr"
            root.sheet.cell(row=17, column= 5).value = "1st"
            root.sheet.cell(row=18, column= 5).value = "2nd"
            root.sheet.cell(row=19, column= 5).value = "Avr"
            root.sheet.cell(row=20, column= 5).value = "1st"
            root.sheet.cell(row=21, column= 5).value = "2nd"
            root.sheet.cell(row=22, column= 5).value = "Avr"
            root.sheet.cell(row=23, column= 5).value = "1st"
            root.sheet.cell(row=24, column= 5).value = "2nd"
            root.sheet.cell(row=25, column= 5).value = "Avr"

            #merge_cells
            root.sheet.merge_cells('A5:A7')
            root.sheet.merge_cells('B5:B7')
            root.sheet.merge_cells('C5:C7')
            root.sheet.merge_cells('D5:D7')

            root.sheet.merge_cells('A8:A10')
            root.sheet.merge_cells('B8:B10')
            root.sheet.merge_cells('C8:C10')
            root.sheet.merge_cells('D8:D10')
            root.sheet.merge_cells('D8:D10')

            root.sheet.merge_cells('A11:A13')
            root.sheet.merge_cells('B11:B13')
            root.sheet.merge_cells('C11:C13')
            root.sheet.merge_cells('D11:D13')
            root.sheet.merge_cells('D11:D13')

            root.sheet.merge_cells('A14:A16')
            root.sheet.merge_cells('B14:B16')
            root.sheet.merge_cells('C14:C16')
            root.sheet.merge_cells('D14:D16')
            root.sheet.merge_cells('D14:D16')

            root.sheet.merge_cells('A17:A19')
            root.sheet.merge_cells('B17:B19')
            root.sheet.merge_cells('C17:C19')
            root.sheet.merge_cells('D17:D19')
            root.sheet.merge_cells('D17:D19')

            root.sheet.merge_cells('A20:A22')
            root.sheet.merge_cells('B20:B22')
            root.sheet.merge_cells('C20:C22')
            root.sheet.merge_cells('D20:D22')
            root.sheet.merge_cells('D20:D22')

            root.sheet.merge_cells('A23:A25')
            root.sheet.merge_cells('B23:B25')
            root.sheet.merge_cells('C23:C25')
            root.sheet.merge_cells('D23:D25')
            root.sheet.merge_cells('D23:D25')

            #column_dimensions
            root.sheet.column_dimensions['B'].width= 25
            root.sheet.column_dimensions['A'].width = 5
            root.sheet.column_dimensions['C'].width = 5
            root.sheet.column_dimensions['D'].width = 5
           
                   
            for b in range(21):
               for c in range(14):
                   root.sheet.cell(row = b+5, column=c+6).value = root.stu1M[8]
 
            root.wb.save('1-7 students.xlsx')   
               
        def Add(root):
                     # page 1
            root.s1 = []  
            root.s2 = []
            
            root.s3 = []  
            root.s4 = []            
            
            root.s5 = []  
            root.s6 = []

            root.s7 = []  
            root.s8 = []
            
            root.s9 = []  
            root.s10 = []
            
            root.s11 = []  
            root.s12 = []
            
            root.s13 = []  
            root.s14 = []
            
            for B in range (11):
                
                x = (root.get_stu1()[B] + root.get_stu1()[B + 14]) / 2 
                root.stu1M[B + 28].delete(0,tk.END)   
                root.stu1M[B + 28].insert(0,x)
                
              
                                
                root.s1.append(root.get_stu1()[B])
                root.s2.append(root.get_stu1()[B + 14])
                
                y = (root.get_stu1()[B+ 42] + root.get_stu1()[B + 56]) / 2 
                root.stu1M[B + 70].delete(0,tk.END)   
                root.stu1M[B + 70].insert(0,y)
                
                root.s3.append(root.get_stu1()[B + 42])
                root.s4.append(root.get_stu1()[B + 56])
                
                z = (root.get_stu1()[B+ 84] + root.get_stu1()[B + 98]) / 2 
                root.stu1M[B + 112].delete(0,tk.END)   
                root.stu1M[B + 112].insert(0,z)
                
                root.s5.append(root.get_stu1()[B+ 84])
                root.s6.append(root.get_stu1()[B + 98])
                
                a = (root.get_stu1()[B+ 126] + root.get_stu1()[B + 140]) / 2 
                root.stu1M[B + 154].delete(0,tk.END)   
                root.stu1M[B + 154].insert(0,a)
                
                root.s7.append(root.get_stu1()[B+ 126])
                root.s8.append(root.get_stu1()[B + 140])
                
                b = (root.get_stu1()[B+ 168] + root.get_stu1()[B + 182]) / 2 
                root.stu1M[B + 196].delete(0,tk.END)   
                root.stu1M[B + 196].insert(0,b)
                
                root.s9.append(root.get_stu1()[B + 168])
                root.s10.append(root.get_stu1()[B + 182])
                
                c = (root.get_stu1()[B+ 210] + root.get_stu1()[B + 224]) / 2 
                root.stu1M[B + 238].delete(0,tk.END)   
                root.stu1M[B + 238].insert(0,c)
                
                root.s11.append(root.get_stu1()[B + 210])
                root.s12.append(root.get_stu1()[B + 224])
                
                d = (root.get_stu1()[B+ 252] + root.get_stu1()[B + 266]) / 2 
                root.stu1M[B + 280].delete(0,tk.END)   
                root.stu1M[B + 280].insert(0,d)
                
                root.s13.append(root.get_stu1()[B + 252])
                root.s14.append(root.get_stu1()[B + 266])
                
                
            root.sum =[  sum(root.s1),  round(sum(root.s1)/11,2),  sum(root.s2),  round(sum(root.s2)/11,2),
                         sum(root.s3),  round(sum(root.s3)/11,2),  sum(root.s4),  round(sum(root.s4)/11,2),
                         sum(root.s5),  round(sum(root.s5)/11,2),  sum(root.s6),  round(sum(root.s6)/11,2), 
                         sum(root.s7),  round(sum(root.s7)/11,2),   sum(root.s8),  round(sum(root.s8)/11,2),
                         sum(root.s9),  round(sum(root.s9)/11,2),   sum(root.s10), round(sum(root.s10)/11,2),
                         sum(root.s11), round(sum(root.s11)/11,2),  sum(root.s12),  round(sum(root.s12)/11,2),
                         sum(root.s13), round(sum(root.s13)/11,2),  sum(root.s14), round(sum(root.s14)/11,2)] 
                                    
            root.TAVR =[ (sum(root.s1)+sum(root.s2))/2,   round((root.sum[1] + root.sum[3])/2,2), 
                         (sum(root.s3)+sum(root.s4))/2,   round((root.sum[5] + root.sum[7])/2,2),                           
                         (sum(root.s5)+sum(root.s6))/2,   round((root.sum[9] + root.sum[11])/2,2),  
                         (sum(root.s7)+sum(root.s8))/2,   round((root.sum[13] + root.sum[15])/2,2),                         
                         (sum(root.s9)+sum(root.s10))/2,  round((root.sum[17] + root.sum[19])/2,2), 
                         (sum(root.s11)+sum(root.s12))/2, round((root.sum[21] + root.sum[23])/2,2),                          
                         (sum(root.s13)+sum(root.s14))/2, round((root.sum[25] + root.sum[27])/2,2)] 
          
            
            for g in range(2):
                root.stu1M[g +11].delete(0, tk.END)
                root.stu1M[g +11].insert(0, root.sum[g])
                
                root.stu1M[g +25].delete(0, tk.END)
                root.stu1M[g +25].insert(0, root.sum[g+2])
            
                root.stu1M[g +39].delete(0, tk.END)
                root.stu1M[g +39].insert(0, root.TAVR[g])            
                root.stu1M[g +81].delete(0, tk.END)
                root.stu1M[g +81].insert(0, root.TAVR[g+2]) 
                root.stu1M[g +123].delete(0, tk.END)
                root.stu1M[g +123].insert(0, root.TAVR[g+4])
                root.stu1M[g +165].delete(0, tk.END)
                root.stu1M[g +165].insert(0, root.TAVR[g+6])
                root.stu1M[g +207].delete(0, tk.END)
                root.stu1M[g +207].insert(0, root.TAVR[g+8])
                root.stu1M[g +249].delete(0, tk.END)
                root.stu1M[g +249].insert(0, root.TAVR[g+10])
                root.stu1M[g +291].delete(0, tk.END)
                root.stu1M[g +291].insert(0, root.TAVR[g+12])                 
                
                root.stu1M[g +53].delete(0, tk.END)
                root.stu1M[g +53].insert(0, root.sum[g+4])
            
                root.stu1M[g +67].delete(0, tk.END)
                root.stu1M[g +67].insert(0, root.sum[g+6])
            
                root.stu1M[g +95].delete(0, tk.END)
                root.stu1M[g +95].insert(0, root.sum[g+8])
                
                root.stu1M[g +109].delete(0, tk.END)
                root.stu1M[g +109].insert(0, root.sum[g+10])
                
                root.stu1M[g +137].delete(0, tk.END)
                root.stu1M[g +137].insert(0, root.sum[g+12])
                
                root.stu1M[g +151].delete(0, tk.END)
                root.stu1M[g +151].insert(0, root.sum[g+14])
            
                root.stu1M[g +179].delete(0, tk.END)
                root.stu1M[g +179].insert(0, root.sum[g+16])
                
                root.stu1M[g +193].delete(0, tk.END)
                root.stu1M[g +193].insert(0, root.sum[g+18])
            
                root.stu1M[g +221].delete(0, tk.END)
                root.stu1M[g +221].insert(0, root.sum[g+20])
            
                root.stu1M[g +235].delete(0, tk.END)
                root.stu1M[g +235].insert(0, root.sum[g+22])
                
                root.stu1M[g +263].delete(0, tk.END)
                root.stu1M[g +263].insert(0, root.sum[g+24])
                
                root.stu1M[g +277].delete(0, tk.END)
                root.stu1M[g +277].insert(0, root.sum[g+26])
                
            
                
                # page2
                
                
                root.s15 = []  
                root.s16 = []
                    
                root.s17 = []  
                root.s18 = []            
                    
                root.s19 = []  
                root.s20 = []

                root.s21 = []  
                root.s22 = []
                    
                root.s23 = []  
                root.s24 = []
                    
                root.s25 = []  
                root.s26 = []
                    
                root.s27 = []  
                root.s28 = []
                    
                for B in range (11):
                        
                        x = (root.get_stu2()[B] + root.get_stu2()[B + 14]) / 2 
                        root.stu2M[B + 28].delete(0,tk.END)   
                        root.stu2M[B + 28].insert(0,x)     
                      
                                        
                        root.s15.append(root.get_stu2()[B])
                        root.s16.append(root.get_stu2()[B + 14])
                        
                        y = (root.get_stu2()[B+ 42] + root.get_stu2()[B + 56]) / 2 
                        root.stu2M[B + 70].delete(0,tk.END)   
                        root.stu2M[B + 70].insert(0,y)
                        
                        root.s17.append(root.get_stu2()[B + 42])
                        root.s18.append(root.get_stu2()[B + 56])
                        
                        z = (root.get_stu2()[B+ 84] + root.get_stu2()[B + 98]) / 2 
                        root.stu2M[B + 112].delete(0,tk.END)   
                        root.stu2M[B + 112].insert(0,z)
                        
                        root.s19.append(root.get_stu2()[B+ 84])
                        root.s20.append(root.get_stu2()[B + 98])
                        
                        a = (root.get_stu2()[B+ 126] + root.get_stu2()[B + 140]) / 2 
                        root.stu2M[B + 154].delete(0,tk.END)   
                        root.stu2M[B + 154].insert(0,a)
                        
                        root.s21.append(root.get_stu2()[B+ 126])
                        root.s22.append(root.get_stu2()[B + 140])
                        
                        b = (root.get_stu2()[B+ 168] + root.get_stu2()[B + 182]) / 2 
                        root.stu2M[B + 196].delete(0,tk.END)   
                        root.stu2M[B + 196].insert(0,b)
                        
                        root.s23.append(root.get_stu2()[B + 168])
                        root.s24.append(root.get_stu2()[B + 182])
                        
                        c = (root.get_stu2()[B+ 210] + root.get_stu2()[B + 224]) / 2 
                        root.stu2M[B + 238].delete(0,tk.END)   
                        root.stu2M[B + 238].insert(0,c)
                        
                        root.s25.append(root.get_stu2()[B + 210])
                        root.s26.append(root.get_stu2()[B + 224])
                        
                        d = (root.get_stu2()[B+ 252] + root.get_stu2()[B + 266]) / 2 
                        root.stu2M[B + 280].delete(0,tk.END)   
                        root.stu2M[B + 280].insert(0,d)
                        
                        root.s27.append(root.get_stu2()[B + 252])
                        root.s28.append(root.get_stu2()[B + 266])
                        
                root.sum2 =    [ sum(root.s15),  round(sum(root.s15)/11,2),  sum(root.s16),  round(sum(root.s16)/11,2),
                                 sum(root.s17),  round(sum(root.s17)/11,2),  sum(root.s18),  round(sum(root.s18)/11,2),
                                 sum(root.s19),  round(sum(root.s19)/11,2),  sum(root.s20),  round(sum(root.s20)/11,2), 
                                 sum(root.s21),  round(sum(root.s21)/11,2),  sum(root.s22),  round(sum(root.s22)/11,2),
                                 sum(root.s23),  round(sum(root.s23)/11,2),  sum(root.s24),  round(sum(root.s24)/11,2),
                                 sum(root.s25),  round(sum(root.s25)/11,2),  sum(root.s26),  round(sum(root.s26)/11,2),
                                 sum(root.s27),  round(sum(root.s27)/11,2),  sum(root.s28),  round(sum(root.s28)/11,2)] 
                                            
                root.TAVR2 =[    (sum(root.s15)+sum(root.s16))/2,   round((root.sum2[1] +  root.sum2[3])/2,2), 
                                 (sum(root.s17)+sum(root.s18))/2,   round((root.sum2[5] +  root.sum2[7])/2,2),                          
                                 (sum(root.s19)+sum(root.s20))/2,   round((root.sum2[9] +  root.sum2[11])/2,2),  
                                 (sum(root.s21)+sum(root.s22))/2,   round((root.sum2[13] + root.sum2[15])/2,2),                         
                                 (sum(root.s23)+sum(root.s24))/2,   round((root.sum2[17] + root.sum2[19])/2,2), 
                                 (sum(root.s25)+sum(root.s26))/2,   round((root.sum2[21] + root.sum2[23])/2,2),                          
                                 (sum(root.s27)+sum(root.s28))/2,   round((root.sum2[25] + root.sum2[27])/2,2)] 
                  
                    
                for g in range(2):
                        root.stu2M[g +11].delete(0, tk.END)
                        root.stu2M[g +11].insert(0, root.sum2[g])
                        
                        root.stu2M[g +25].delete(0, tk.END)
                        root.stu2M[g +25].insert(0, root.sum2[g+2])
                    
                        root.stu2M[g +39].delete(0, tk.END)
                        root.stu2M[g +39].insert(0, root.TAVR2[g])            
                        root.stu2M[g +81].delete(0, tk.END)
                        root.stu2M[g +81].insert(0, root.TAVR2[g+2]) 
                        root.stu2M[g +123].delete(0, tk.END)
                        root.stu2M[g +123].insert(0, root.TAVR2[g+4])
                        root.stu2M[g +165].delete(0, tk.END)
                        root.stu2M[g +165].insert(0, root.TAVR2[g+6])
                        root.stu2M[g +207].delete(0, tk.END)
                        root.stu2M[g +207].insert(0, root.TAVR2[g+8])
                        root.stu2M[g +249].delete(0, tk.END)
                        root.stu2M[g +249].insert(0, root.TAVR2[g+10])
                        root.stu2M[g +291].delete(0, tk.END)
                        root.stu2M[g +291].insert(0, root.TAVR2[g+12])                 
                        
                        root.stu2M[g +53].delete(0, tk.END)
                        root.stu2M[g +53].insert(0, root.sum2[g+4])
                    
                        root.stu2M[g +67].delete(0, tk.END)
                        root.stu2M[g +67].insert(0, root.sum2[g+6])
                    
                        root.stu2M[g +95].delete(0, tk.END)
                        root.stu2M[g +95].insert(0, root.sum2[g+8])
                        
                        root.stu2M[g +109].delete(0, tk.END)
                        root.stu2M[g +109].insert(0, root.sum2[g+10])
                        
                        root.stu2M[g +137].delete(0, tk.END)
                        root.stu2M[g +137].insert(0, root.sum2[g+12])
                        
                        root.stu2M[g +151].delete(0, tk.END)
                        root.stu2M[g +151].insert(0, root.sum2[g+14])
                    
                        root.stu2M[g +179].delete(0, tk.END)
                        root.stu2M[g +179].insert(0, root.sum2[g+16])
                        
                        root.stu2M[g +193].delete(0, tk.END)
                        root.stu2M[g +193].insert(0, root.sum2[g+18])
                    
                        root.stu2M[g +221].delete(0, tk.END)
                        root.stu2M[g +221].insert(0, root.sum2[g+20])
                    
                        root.stu2M[g +235].delete(0, tk.END)
                        root.stu2M[g +235].insert(0, root.sum2[g+22])
                        
                        root.stu2M[g +263].delete(0, tk.END)
                        root.stu2M[g +263].insert(0, root.sum2[g+24])
                        
                        root.stu2M[g +277].delete(0, tk.END)
                        root.stu2M[g +277].insert(0, root.sum2[g+26])
                        
                        
                         # page3
                
                
                root.s29 = []  
                root.s30 = []
                    
                root.s31 = []  
                root.s32 = []            
                    
                root.s33 = []  
                root.s34 = []

                root.s35 = []  
                root.s36 = []
                    
                root.s37 = []  
                root.s38 = []
                    
                root.s39 = []  
                root.s40 = []
                    
                root.s41 = []  
                root.s42 = []
                    
                for B in range (11):
                        
                        x = (root.get_stu3()[B] + root.get_stu3()[B + 14]) / 2 
                        root.stu3M[B + 28].delete(0,tk.END)   
                        root.stu3M[B + 28].insert(0,x)     
                      
                                        
                        root.s29.append(root.get_stu3()[B])
                        root.s30.append(root.get_stu3()[B + 14])
                        
                        y = (root.get_stu3()[B+ 42] + root.get_stu3()[B + 56]) / 2 
                        root.stu3M[B + 70].delete(0,tk.END)   
                        root.stu3M[B + 70].insert(0,y)
                        
                        root.s31.append(root.get_stu3()[B + 42])
                        root.s32.append(root.get_stu3()[B + 56])
                        
                        z = (root.get_stu3()[B+ 84] + root.get_stu3()[B + 98]) / 2 
                        root.stu3M[B + 112].delete(0,tk.END)   
                        root.stu3M[B + 112].insert(0,z)
                        
                        root.s33.append(root.get_stu3()[B+ 84])
                        root.s34.append(root.get_stu3()[B + 98])
                        
                        a = (root.get_stu3()[B+ 126] + root.get_stu3()[B + 140]) / 2 
                        root.stu3M[B + 154].delete(0,tk.END)   
                        root.stu3M[B + 154].insert(0,a)
                        
                        root.s35.append(root.get_stu3()[B+ 126])
                        root.s36.append(root.get_stu3()[B + 140])
                        
                        b = (root.get_stu3()[B+ 168] + root.get_stu3()[B + 182]) / 2 
                        root.stu3M[B + 196].delete(0,tk.END)   
                        root.stu3M[B + 196].insert(0,b)
                        
                        root.s37.append(root.get_stu3()[B + 168])
                        root.s38.append(root.get_stu3()[B + 182])
                        
                        c = (root.get_stu3()[B+ 210] + root.get_stu3()[B + 224]) / 2 
                        root.stu3M[B + 238].delete(0,tk.END)   
                        root.stu3M[B + 238].insert(0,c)
                        
                        root.s39.append(root.get_stu3()[B + 210])
                        root.s40.append(root.get_stu3()[B + 224])
                        
                        d = (root.get_stu3()[B+ 252] + root.get_stu3()[B + 266]) / 2 
                        root.stu3M[B + 280].delete(0,tk.END)   
                        root.stu3M[B + 280].insert(0,d)
                        
                        root.s41.append(root.get_stu3()[B + 252])
                        root.s42.append(root.get_stu3()[B + 266])
                        
                root.sum3 =    [ sum(root.s29),  round(sum(root.s29)/11,2),  sum(root.s30),  round(sum(root.s30)/11,2),
                                 sum(root.s31),  round(sum(root.s31)/11,2),  sum(root.s32),  round(sum(root.s32)/11,2),
                                 sum(root.s33),  round(sum(root.s33)/11,2),  sum(root.s34),  round(sum(root.s34)/11,2), 
                                 sum(root.s35),  round(sum(root.s35)/11,2),  sum(root.s36),  round(sum(root.s36)/11,2),
                                 sum(root.s37),  round(sum(root.s37)/11,2),  sum(root.s38),  round(sum(root.s38)/11,2),
                                 sum(root.s39),  round(sum(root.s39)/11,2),  sum(root.s40),  round(sum(root.s40)/11,2),
                                 sum(root.s41),  round(sum(root.s41)/11,2),  sum(root.s42),  round(sum(root.s42)/11,2)] 
                                            
                root.TAVR3 =[   (sum(root.s29)+sum(root.s30))/2,    round((root.sum3[1] +  root.sum3[3])/2,2), 
                                 (sum(root.s31)+sum(root.s32))/2,   round((root.sum3[5] +  root.sum3[7])/2,2),                           
                                 (sum(root.s33)+sum(root.s34))/2,   round((root.sum3[9] +  root.sum3[11])/2,2),  
                                 (sum(root.s35)+sum(root.s36))/2,   round((root.sum3[13] + root.sum3[15])/2,2),                         
                                 (sum(root.s37)+sum(root.s38))/2,   round((root.sum3[17] + root.sum3[19])/2,2), 
                                 (sum(root.s39)+sum(root.s40))/2,   round((root.sum3[21] + root.sum3[23])/2,2),                          
                                 (sum(root.s41)+sum(root.s42))/2,   round((root.sum3[25] + root.sum3[27])/2,2)] 
                  
                    
                for g in range(2):
                        root.stu3M[g +11].delete(0, tk.END)
                        root.stu3M[g +11].insert(0, root.sum3[g])
                        
                        root.stu3M[g +25].delete(0, tk.END)
                        root.stu3M[g +25].insert(0, root.sum3[g+2])
                    
                        root.stu3M[g +39].delete(0, tk.END)
                        root.stu3M[g +39].insert(0, root.TAVR3[g])            
                        root.stu3M[g +81].delete(0, tk.END)
                        root.stu3M[g +81].insert(0, root.TAVR3[g+2]) 
                        root.stu3M[g +123].delete(0, tk.END)
                        root.stu3M[g +123].insert(0, root.TAVR3[g+4])
                        root.stu3M[g +165].delete(0, tk.END)
                        root.stu3M[g +165].insert(0, root.TAVR3[g+6])
                        root.stu3M[g +207].delete(0, tk.END)
                        root.stu3M[g +207].insert(0, root.TAVR3[g+8])
                        root.stu3M[g +249].delete(0, tk.END)
                        root.stu3M[g +249].insert(0, root.TAVR3[g+10])
                        root.stu3M[g +291].delete(0, tk.END)
                        root.stu3M[g +291].insert(0, root.TAVR3[g+12])                 
                        
                        root.stu3M[g +53].delete(0, tk.END)
                        root.stu3M[g +53].insert(0, root.sum3[g+4])
                    
                        root.stu3M[g +67].delete(0, tk.END)
                        root.stu3M[g +67].insert(0, root.sum3[g+6])
                    
                        root.stu3M[g +95].delete(0, tk.END)
                        root.stu3M[g +95].insert(0, root.sum3[g+8])
                        
                        root.stu3M[g +109].delete(0, tk.END)
                        root.stu3M[g +109].insert(0, root.sum3[g+10])
                        
                        root.stu3M[g +137].delete(0, tk.END)
                        root.stu3M[g +137].insert(0, root.sum3[g+12])
                        
                        root.stu3M[g +151].delete(0, tk.END)
                        root.stu3M[g +151].insert(0, root.sum3[g+14])
                    
                        root.stu3M[g +179].delete(0, tk.END)
                        root.stu3M[g +179].insert(0, root.sum3[g+16])
                        
                        root.stu3M[g +193].delete(0, tk.END)
                        root.stu3M[g +193].insert(0, root.sum3[g+18])
                    
                        root.stu3M[g +221].delete(0, tk.END)
                        root.stu3M[g +221].insert(0, root.sum3[g+20])
                    
                        root.stu3M[g +235].delete(0, tk.END)
                        root.stu3M[g +235].insert(0, root.sum3[g+22])
                        
                        root.stu3M[g +263].delete(0, tk.END)
                        root.stu3M[g +263].insert(0, root.sum3[g+24])
                        
                        root.stu3M[g +277].delete(0, tk.END)
                        root.stu3M[g +277].insert(0, root.sum3[g+26])        
                 




                 # page4
                
                
                root.s43 = []  
                root.s44 = []
                    
                root.s45 = []  
                root.s46 = []            
                    
                root.s47 = []  
                root.s48 = []

                root.s49 = []  
                root.s50 = []
                    
                root.s51 = []  
                root.s52 = []
                    
                root.s53= []  
                root.s54 = []
                    
                root.s55 = []  
                root.s56 = []
                    
                for B in range (11):
                        
                        x = (root.get_stu4()[B] + root.get_stu4()[B + 14]) / 2 
                        root.stu4M[B + 28].delete(0,tk.END)   
                        root.stu4M[B + 28].insert(0,x)     
                      
                                        
                        root.s43.append(root.get_stu4()[B])
                        root.s44.append(root.get_stu4()[B + 14])
                        
                        y = (root.get_stu4()[B+ 42] + root.get_stu4()[B + 56]) / 2 
                        root.stu4M[B + 70].delete(0,tk.END)   
                        root.stu4M[B + 70].insert(0,y)
                        
                        root.s45.append(root.get_stu4()[B + 42])
                        root.s46.append(root.get_stu4()[B + 56])
                        
                        z = (root.get_stu4()[B+ 84] + root.get_stu4()[B + 98]) / 2 
                        root.stu4M[B + 112].delete(0,tk.END)   
                        root.stu4M[B + 112].insert(0,z)
                        
                        root.s47.append(root.get_stu4()[B+ 84])
                        root.s48.append(root.get_stu4()[B + 98])
                        
                        a = (root.get_stu4()[B+ 126] + root.get_stu4()[B + 140]) / 2 
                        root.stu4M[B + 154].delete(0,tk.END)   
                        root.stu4M[B + 154].insert(0,a)
                        
                        root.s49.append(root.get_stu4()[B+ 126])
                        root.s50.append(root.get_stu4()[B + 140])
                        
                        b = (root.get_stu4()[B+ 168] + root.get_stu4()[B + 182]) / 2 
                        root.stu4M[B + 196].delete(0,tk.END)   
                        root.stu4M[B + 196].insert(0,b)
                        
                        root.s51.append(root.get_stu4()[B + 168])
                        root.s52.append(root.get_stu4()[B + 182])
                        
                        c = (root.get_stu4()[B+ 210] + root.get_stu4()[B + 224]) / 2 
                        root.stu4M[B + 238].delete(0,tk.END)   
                        root.stu4M[B + 238].insert(0,c)
                        
                        root.s53.append(root.get_stu4()[B + 210])
                        root.s54.append(root.get_stu4()[B + 224])
                        
                        d = (root.get_stu4()[B+ 252] + root.get_stu4()[B + 266]) / 2 
                        root.stu4M[B + 280].delete(0,tk.END)   
                        root.stu4M[B + 280].insert(0,d)
                        
                        root.s55.append(root.get_stu4()[B + 252])
                        root.s56.append(root.get_stu4()[B + 266])
                        
                root.sum4 =    [ sum(root.s43),  round(sum(root.s43)/11,2),  sum(root.s44),  round(sum(root.s44)/11,2),
                                 sum(root.s45),  round(sum(root.s45)/11,2),  sum(root.s46),  round(sum(root.s46)/11,2),
                                 sum(root.s47),  round(sum(root.s47)/11,2),  sum(root.s48),  round(sum(root.s48)/11,2), 
                                 sum(root.s49),  round(sum(root.s49)/11,2),  sum(root.s50),  round(sum(root.s50)/11,2),
                                 sum(root.s51),  round(sum(root.s51)/11,2),  sum(root.s52),  round(sum(root.s52)/11,2),
                                 sum(root.s53),  round(sum(root.s53)/11,2),  sum(root.s54),  round(sum(root.s54)/11,2),
                                 sum(root.s55),  round(sum(root.s55)/11,2),  sum(root.s56),  round(sum(root.s56)/11,2)] 
                                            
                root.TAVR4 =[   (sum(root.s43)+sum(root.s44))/2,    round((root.sum4[1] +  root.sum4[3])/2,2), 
                                 (sum(root.s45)+sum(root.s46))/2,   round((root.sum4[5] +  root.sum4[7])/2,2),                           
                                 (sum(root.s47)+sum(root.s48))/2,   round((root.sum4[9] +  root.sum4[11])/2,2),  
                                 (sum(root.s49)+sum(root.s50))/2,   round((root.sum4[13] + root.sum4[15])/2,2),                         
                                 (sum(root.s51)+sum(root.s52))/2,   round((root.sum4[17] + root.sum4[19])/2,2), 
                                 (sum(root.s53)+sum(root.s54))/2,   round((root.sum4[21] + root.sum4[23])/2,2),                          
                                 (sum(root.s55)+sum(root.s56))/2,   round((root.sum4[25] + root.sum4[27])/2,2)] 
                  
                    
                for g in range(2):
                        root.stu4M[g +11].delete(0, tk.END)
                        root.stu4M[g +11].insert(0, root.sum4[g])
                        root.stu4M[g +25].delete(0, tk.END)
                        root.stu4M[g +25].insert(0, root.sum4[g+2])                    
                        root.stu4M[g +39].delete(0, tk.END)
                        root.stu4M[g +39].insert(0, root.TAVR4[g])            
                        root.stu4M[g +81].delete(0, tk.END)
                        root.stu4M[g +81].insert(0, root.TAVR4[g+2]) 
                        root.stu4M[g +123].delete(0, tk.END)
                        root.stu4M[g +123].insert(0, root.TAVR4[g+4])
                        root.stu4M[g +165].delete(0, tk.END)
                        root.stu4M[g +165].insert(0, root.TAVR4[g+6])
                        root.stu4M[g +207].delete(0, tk.END)
                        root.stu4M[g +207].insert(0, root.TAVR4[g+8])
                        root.stu4M[g +249].delete(0, tk.END)
                        root.stu4M[g +249].insert(0, root.TAVR4[g+10])
                        root.stu4M[g +291].delete(0, tk.END)
                        root.stu4M[g +291].insert(0, root.TAVR4[g+12])                                         
                        root.stu4M[g +53].delete(0, tk.END)
                        root.stu4M[g +53].insert(0, root.sum4[g+4])
                        root.stu4M[g +67].delete(0, tk.END)
                        root.stu4M[g +67].insert(0, root.sum4[g+6])
                        root.stu4M[g +95].delete(0, tk.END)
                        root.stu4M[g +95].insert(0, root.sum4[g+8])
                        root.stu4M[g +109].delete(0, tk.END)
                        root.stu4M[g +109].insert(0, root.sum4[g+10])
                        root.stu4M[g +137].delete(0, tk.END)
                        root.stu4M[g +137].insert(0, root.sum4[g+12])
                        root.stu4M[g +151].delete(0, tk.END)
                        root.stu4M[g +151].insert(0, root.sum4[g+14])
                        root.stu4M[g +179].delete(0, tk.END)
                        root.stu4M[g +179].insert(0, root.sum4[g+16])
                        root.stu4M[g +193].delete(0, tk.END)
                        root.stu4M[g +193].insert(0, root.sum4[g+18])
                        root.stu4M[g +221].delete(0, tk.END)
                        root.stu4M[g +221].insert(0, root.sum4[g+20])
                        root.stu4M[g +235].delete(0, tk.END)
                        root.stu4M[g +235].insert(0, root.sum4[g+22])
                        root.stu4M[g +263].delete(0, tk.END)
                        root.stu4M[g +263].insert(0, root.sum4[g+24])
                        root.stu4M[g +277].delete(0, tk.END)
                        root.stu4M[g +277].insert(0, root.sum4[g+26]) 
                                 
                
                
                
                
                
                
                 # page5
                
                
                root.s57 = []  
                root.s58 = []
                    
                root.s59 = []  
                root.s60 = []            
                    
                root.s61 = []  
                root.s62 = []

                root.s63 = []  
                root.s64 = []
                    
                root.s65 = []  
                root.s66 = []
                    
                root.s67= []  
                root.s68 = []
                    
                root.s69 = []  
                root.s70 = []
                    
                for B in range (11):
                        
                        x = (root.get_stu5()[B] + root.get_stu5()[B + 14]) / 2 
                        root.stu5M[B + 28].delete(0,tk.END)   
                        root.stu5M[B + 28].insert(0,x)     
                      
                                        
                        root.s57.append(root.get_stu5()[B])
                        root.s58.append(root.get_stu5()[B + 14])
                        
                        y = (root.get_stu5()[B+ 42] + root.get_stu5()[B + 56]) / 2 
                        root.stu5M[B + 70].delete(0,tk.END)   
                        root.stu5M[B + 70].insert(0,y)
                        
                        root.s59.append(root.get_stu5()[B + 42])
                        root.s60.append(root.get_stu5()[B + 56])
                        
                        z = (root.get_stu5()[B+ 84] + root.get_stu5()[B + 98]) / 2 
                        root.stu5M[B + 112].delete(0,tk.END)   
                        root.stu5M[B + 112].insert(0,z)
                        
                        root.s61.append(root.get_stu5()[B+ 84])
                        root.s62.append(root.get_stu5()[B + 98])
                        
                        a = (root.get_stu5()[B+ 126] + root.get_stu5()[B + 140]) / 2 
                        root.stu5M[B + 154].delete(0,tk.END)   
                        root.stu5M[B + 154].insert(0,a)
                        
                        root.s63.append(root.get_stu5()[B+ 126])
                        root.s64.append(root.get_stu5()[B + 140])
                        
                        b = (root.get_stu5()[B+ 168] + root.get_stu5()[B + 182]) / 2 
                        root.stu5M[B + 196].delete(0,tk.END)   
                        root.stu5M[B + 196].insert(0,b)
                        
                        root.s65.append(root.get_stu5()[B + 168])
                        root.s66.append(root.get_stu5()[B + 182])
                        
                        c = (root.get_stu5()[B+ 210] + root.get_stu5()[B + 224]) / 2 
                        root.stu5M[B + 238].delete(0,tk.END)   
                        root.stu5M[B + 238].insert(0,c)
                        
                        root.s67.append(root.get_stu5()[B + 210])
                        root.s68.append(root.get_stu5()[B + 224])
                        
                        d = (root.get_stu5()[B+ 252] + root.get_stu5()[B + 266]) / 2 
                        root.stu5M[B + 280].delete(0,tk.END)   
                        root.stu5M[B + 280].insert(0,d)
                        
                        root.s69.append(root.get_stu5()[B + 252])
                        root.s70.append(root.get_stu5()[B + 266])
                        
                root.sum5 =    [ sum(root.s57),  round(sum(root.s57)/11,2),  sum(root.s58),  round(sum(root.s58)/11,2),
                                 sum(root.s59),  round(sum(root.s59)/11,2),  sum(root.s60),  round(sum(root.s60)/11,2),
                                 sum(root.s61),  round(sum(root.s61)/11,2),  sum(root.s62),  round(sum(root.s62)/11,2), 
                                 sum(root.s63),  round(sum(root.s63)/11,2),  sum(root.s64),  round(sum(root.s64)/11,2),
                                 sum(root.s65),  round(sum(root.s65)/11,2),  sum(root.s66),  round(sum(root.s66)/11,2),
                                 sum(root.s67),  round(sum(root.s67)/11,2),  sum(root.s68),  round(sum(root.s68)/11,2),
                                 sum(root.s69),  round(sum(root.s69)/11,2),  sum(root.s70),  round(sum(root.s70)/11,2)] 
                                            
                root.TAVR5 =[    (sum(root.s57)+sum(root.s58))/2,   round((root.sum5[1] +  root.sum5[3])/2,2), 
                                 (sum(root.s59)+sum(root.s60))/2,   round((root.sum5[5] +  root.sum5[7])/2,2),                          
                                 (sum(root.s61)+sum(root.s62))/2,   round((root.sum5[9] +  root.sum5[11])/2,2),  
                                 (sum(root.s63)+sum(root.s64))/2,   round((root.sum5[13] + root.sum5[15])/2,2),                         
                                 (sum(root.s65)+sum(root.s66))/2,   round((root.sum5[17] + root.sum5[19])/2,2), 
                                 (sum(root.s67)+sum(root.s68))/2,   round((root.sum5[21] + root.sum5[23])/2,2),                          
                                 (sum(root.s69)+sum(root.s70))/2,   round((root.sum5[25] + root.sum5[27])/2,2)] 
                  
                    
                for g in range(2):
                        root.stu5M[g +11].delete(0, tk.END)
                        root.stu5M[g +11].insert(0, root.sum5[g])
                        root.stu5M[g +25].delete(0, tk.END)
                        root.stu5M[g +25].insert(0, root.sum5[g+2])                    
                        root.stu5M[g +39].delete(0, tk.END)
                        root.stu5M[g +39].insert(0, root.TAVR5[g])            
                        root.stu5M[g +81].delete(0, tk.END)
                        root.stu5M[g +81].insert(0, root.TAVR5[g+2]) 
                        root.stu5M[g +123].delete(0, tk.END)
                        root.stu5M[g +123].insert(0, root.TAVR5[g+4])
                        root.stu5M[g +165].delete(0, tk.END)
                        root.stu5M[g +165].insert(0, root.TAVR5[g+6])
                        root.stu5M[g +207].delete(0, tk.END)
                        root.stu5M[g +207].insert(0, root.TAVR5[g+8])
                        root.stu5M[g +249].delete(0, tk.END)
                        root.stu5M[g +249].insert(0, root.TAVR5[g+10])
                        root.stu5M[g +291].delete(0, tk.END)
                        root.stu5M[g +291].insert(0, root.TAVR5[g+12])                                         
                        root.stu5M[g +53].delete(0, tk.END)
                        root.stu5M[g +53].insert(0, root.sum5[g+4])
                        root.stu5M[g +67].delete(0, tk.END)
                        root.stu5M[g +67].insert(0, root.sum5[g+6])
                        root.stu5M[g +95].delete(0, tk.END)
                        root.stu5M[g +95].insert(0, root.sum5[g+8])
                        root.stu5M[g +109].delete(0, tk.END)
                        root.stu5M[g +109].insert(0, root.sum5[g+10])
                        root.stu5M[g +137].delete(0, tk.END)
                        root.stu5M[g +137].insert(0, root.sum5[g+12])
                        root.stu5M[g +151].delete(0, tk.END)
                        root.stu5M[g +151].insert(0, root.sum5[g+14])
                        root.stu5M[g +179].delete(0, tk.END)
                        root.stu5M[g +179].insert(0, root.sum5[g+16])
                        root.stu5M[g +193].delete(0, tk.END)
                        root.stu5M[g +193].insert(0, root.sum5[g+18])
                        root.stu5M[g +221].delete(0, tk.END)
                        root.stu5M[g +221].insert(0, root.sum5[g+20])
                        root.stu5M[g +235].delete(0, tk.END)
                        root.stu5M[g +235].insert(0, root.sum5[g+22])
                        root.stu5M[g +263].delete(0, tk.END)
                        root.stu5M[g +263].insert(0, root.sum5[g+24])
                        root.stu5M[g +277].delete(0, tk.END)
                        root.stu5M[g +277].insert(0, root.sum5[g+26]) 
                
                
                # page6
                
                
                root.s71 = []  
                root.s72 = []
                    
                root.s73 = []  
                root.s74 = []            
                    
                root.s75 = []  
                root.s76 = []

                root.s77 = []  
                root.s78 = []
                    
                root.s79 = []  
                root.s80 = []
                    
                root.s81 = []  
                root.s82 = []
                    
                root.s83 = []  
                root.s84 = []
                    
                for B in range (11):
                        
                        x = (root.get_stu6()[B] + root.get_stu6()[B + 14]) / 2 
                        root.stu6M[B + 28].delete(0,tk.END)   
                        root.stu6M[B + 28].insert(0,x)     
                      
                                        
                        root.s71.append(root.get_stu6()[B])
                        root.s72.append(root.get_stu6()[B + 14])
                        
                        y = (root.get_stu6()[B+ 42] + root.get_stu6()[B + 56]) / 2 
                        root.stu6M[B + 70].delete(0,tk.END)   
                        root.stu6M[B + 70].insert(0,y)
                        
                        root.s73.append(root.get_stu6()[B + 42])
                        root.s74.append(root.get_stu6()[B + 56])
                        
                        z = (root.get_stu6()[B+ 84] + root.get_stu6()[B + 98]) / 2 
                        root.stu6M[B + 112].delete(0,tk.END)   
                        root.stu6M[B + 112].insert(0,z)
                        
                        root.s75.append(root.get_stu6()[B+ 84])
                        root.s76.append(root.get_stu6()[B + 98])
                        
                        a = (root.get_stu6()[B+ 126] + root.get_stu6()[B + 140]) / 2 
                        root.stu6M[B + 154].delete(0,tk.END)   
                        root.stu6M[B + 154].insert(0,a)
                        
                        root.s77.append(root.get_stu6()[B+ 126])
                        root.s78.append(root.get_stu6()[B + 140])
                        
                        b = (root.get_stu6()[B+ 168] + root.get_stu6()[B + 182]) / 2 
                        root.stu6M[B + 196].delete(0,tk.END)   
                        root.stu6M[B + 196].insert(0,b)
                        
                        root.s79.append(root.get_stu6()[B + 168])
                        root.s80.append(root.get_stu6()[B + 182])
                        
                        c = (root.get_stu6()[B+ 210] + root.get_stu6()[B + 224]) / 2 
                        root.stu6M[B + 238].delete(0,tk.END)   
                        root.stu6M[B + 238].insert(0,c)
                        
                        root.s81.append(root.get_stu6()[B + 210])
                        root.s82.append(root.get_stu6()[B + 224])
                        
                        d = (root.get_stu6()[B+ 252] + root.get_stu6()[B + 266]) / 2 
                        root.stu6M[B + 280].delete(0,tk.END)   
                        root.stu6M[B + 280].insert(0,d)
                        
                        root.s83.append(root.get_stu6()[B + 252])
                        root.s84.append(root.get_stu6()[B + 266])
                        
                root.sum6 =    [ sum(root.s71),  round(sum(root.s71)/11,2),  sum(root.s72),  round(sum(root.s72)/11,2),
                                 sum(root.s73),  round(sum(root.s73)/11,2),  sum(root.s74),  round(sum(root.s74)/11,2),
                                 sum(root.s75),  round(sum(root.s75)/11,2),  sum(root.s76),  round(sum(root.s76)/11,2), 
                                 sum(root.s77),  round(sum(root.s77)/11,2),  sum(root.s78),  round(sum(root.s78)/11,2),
                                 sum(root.s79),  round(sum(root.s79)/11,2),  sum(root.s80),  round(sum(root.s80)/11,2),
                                 sum(root.s81),  round(sum(root.s81)/11,2),  sum(root.s82),  round(sum(root.s82)/11,2),
                                 sum(root.s83),  round(sum(root.s83)/11,2),  sum(root.s84),  round(sum(root.s84)/11,2)] 
                                            
                root.TAVR6 =[    (sum(root.s71)+sum(root.s72))/2,   round((root.sum6[1] +  root.sum6[3])/2,2), 
                                 (sum(root.s73)+sum(root.s74))/2,   round((root.sum6[5] +  root.sum6[7])/2,2),                          
                                 (sum(root.s75)+sum(root.s76))/2,   round((root.sum6[9] +  root.sum6[11])/2,2),  
                                 (sum(root.s77)+sum(root.s78))/2,   round((root.sum6[13] + root.sum6[15])/2,2),                         
                                 (sum(root.s79)+sum(root.s80))/2,   round((root.sum6[17] + root.sum6[19])/2,2), 
                                 (sum(root.s81)+sum(root.s82))/2,   round((root.sum6[21] + root.sum6[23])/2,2),                          
                                 (sum(root.s83)+sum(root.s84))/2,   round((root.sum6[25] + root.sum6[27])/2,2)] 
                  
                    
                for g in range(2):
                        root.stu6M[g +11].delete(0, tk.END)
                        root.stu6M[g +11].insert(0, root.sum6[g])
                        root.stu6M[g +25].delete(0, tk.END)
                        root.stu6M[g +25].insert(0, root.sum6[g+2])                    
                        root.stu6M[g +39].delete(0, tk.END)
                        root.stu6M[g +39].insert(0, root.TAVR6[g])            
                        root.stu6M[g +81].delete(0, tk.END)
                        root.stu6M[g +81].insert(0, root.TAVR6[g+2]) 
                        root.stu6M[g +123].delete(0, tk.END)
                        root.stu6M[g +123].insert(0, root.TAVR6[g+4])
                        root.stu6M[g +165].delete(0, tk.END)
                        root.stu6M[g +165].insert(0, root.TAVR6[g+6])
                        root.stu6M[g +207].delete(0, tk.END)
                        root.stu6M[g +207].insert(0, root.TAVR6[g+8])
                        root.stu6M[g +249].delete(0, tk.END)
                        root.stu6M[g +249].insert(0, root.TAVR6[g+10])
                        root.stu6M[g +291].delete(0, tk.END)
                        root.stu6M[g +291].insert(0, root.TAVR6[g+12])                                         
                        root.stu6M[g +53].delete(0, tk.END)
                        root.stu6M[g +53].insert(0, root.sum6[g+4])
                        root.stu6M[g +67].delete(0, tk.END)
                        root.stu6M[g +67].insert(0, root.sum6[g+6])
                        root.stu6M[g +95].delete(0, tk.END)
                        root.stu6M[g +95].insert(0, root.sum6[g+8])
                        root.stu6M[g +109].delete(0, tk.END)
                        root.stu6M[g +109].insert(0, root.sum6[g+10])
                        root.stu6M[g +137].delete(0, tk.END)
                        root.stu6M[g +137].insert(0, root.sum6[g+12])
                        root.stu6M[g +151].delete(0, tk.END)
                        root.stu6M[g +151].insert(0, root.sum6[g+14])
                        root.stu6M[g +179].delete(0, tk.END)
                        root.stu6M[g +179].insert(0, root.sum6[g+16])
                        root.stu6M[g +193].delete(0, tk.END)
                        root.stu6M[g +193].insert(0, root.sum6[g+18])
                        root.stu6M[g +221].delete(0, tk.END)
                        root.stu6M[g +221].insert(0, root.sum6[g+20])
                        root.stu6M[g +235].delete(0, tk.END)
                        root.stu6M[g +235].insert(0, root.sum6[g+22])
                        root.stu6M[g +263].delete(0, tk.END)
                        root.stu6M[g +263].insert(0, root.sum6[g+24])
                        root.stu6M[g +277].delete(0, tk.END)
                        root.stu6M[g +277].insert(0, root.sum6[g+26]) 
                
                
                
                
                
                # page7
                
                
                root.s85 = []  
                root.s86 = []
                    
                root.s87 = []  
                root.s88 = []            
                    
                root.s89 = []  
                root.s90 = []

                root.s91 = []  
                root.s92 = []
                    
                root.s93 = []  
                root.s94 = []
                    
                root.s95 = []  
                root.s96 = []
                    
                root.s97 = []  
                root.s98 = []
                    
                for B in range (11):
                        
                        x = (root.get_stu7()[B] + root.get_stu7()[B + 14]) / 2 
                        root.stu7M[B + 28].delete(0,tk.END)   
                        root.stu7M[B + 28].insert(0,x)     
                      
                                        
                        root.s85.append(root.get_stu7()[B])
                        root.s86.append(root.get_stu7()[B + 14])
                       
                        
                        y = (root.get_stu7()[B+ 42] + root.get_stu7()[B + 56]) / 2 
                        root.stu7M[B + 70].delete(0,tk.END)   
                        root.stu7M[B + 70].insert(0,y)
                        
                        root.s87.append(root.get_stu7()[B + 42])
                        root.s88.append(root.get_stu7()[B + 56])
                        
                        z = (root.get_stu7()[B+ 84] + root.get_stu7()[B + 98]) / 2 
                        root.stu7M[B + 112].delete(0,tk.END)   
                        root.stu7M[B + 112].insert(0,z)
                        
                        root.s89.append(root.get_stu7()[B+ 84])
                        root.s90.append(root.get_stu7()[B + 98])
                        
                        a = (root.get_stu7()[B+ 126] + root.get_stu7()[B + 140]) / 2 
                        root.stu7M[B + 154].delete(0,tk.END)   
                        root.stu7M[B + 154].insert(0,a)
                        
                        root.s91.append(root.get_stu7()[B+ 126])
                        root.s92.append(root.get_stu7()[B + 140])
                        
                        b = (root.get_stu7()[B+ 168] + root.get_stu7()[B + 182]) / 2 
                        root.stu7M[B + 196].delete(0,tk.END)   
                        root.stu7M[B + 196].insert(0,b)
                        
                        root.s93.append(root.get_stu7()[B + 168])
                        root.s94.append(root.get_stu7()[B + 182])
                        
                        c = (root.get_stu7()[B+ 210] + root.get_stu7()[B + 224]) / 2 
                        root.stu7M[B + 238].delete(0,tk.END)   
                        root.stu7M[B + 238].insert(0,c)
                        
                        root.s95.append(root.get_stu7()[B + 210])
                        root.s96.append(root.get_stu7()[B + 224])
                        
                        d = (root.get_stu7()[B+ 252] + root.get_stu7()[B + 266]) / 2 
                        root.stu7M[B + 280].delete(0,tk.END)   
                        root.stu7M[B + 280].insert(0,d)
                        
                        root.s97.append(root.get_stu7()[B + 252])
                        root.s98.append(root.get_stu7()[B + 266])
                        
                root.sum7 =    [ sum(root.s85),  round(sum(root.s85)/11,2),   sum(root.s86),  round(sum(root.s86)/11,2),
                                 sum(root.s87),  round(sum(root.s87)/11,2),   sum(root.s88),  round(sum(root.s88)/11,2),
                                 sum(root.s89),  round(sum(root.s89)/11,2),   sum(root.s90),  round(sum(root.s90)/11,2),
                                 sum(root.s91),  round(sum(root.s91)/11,2),   sum(root.s92),  round(sum(root.s92)/11,2),
                                 sum(root.s93),  round(sum(root.s93)/11,2),   sum(root.s94),  round(sum(root.s94)/11,2),
                                 sum(root.s95),  round(sum(root.s95)/11,2),   sum(root.s96),  round(sum(root.s96)/11,2),
                                 sum(root.s97),  round(sum(root.s97)/11,2),   sum(root.s98),  round(sum(root.s98)/11,2)] 
                                            
                root.TAVR7 =[    (sum(root.s85)+sum(root.s86))/2,   round((root.sum7[1]  +  root.sum7[3])/2,2), 
                                 (sum(root.s87)+sum(root.s88))/2,   round((root.sum7[5]  +  root.sum7[7])/2,2),                           
                                 (sum(root.s89)+sum(root.s90))/2,   round((root.sum7[9]  +  root.sum7[11])/2,2),  
                                 (sum(root.s91)+sum(root.s92))/2,   round((root.sum7[13] +  root.sum7[15])/2,2),                         
                                 (sum(root.s93)+sum(root.s94))/2,   round((root.sum7[17] +  root.sum7[19])/2,2), 
                                 (sum(root.s95)+sum(root.s96))/2,   round((root.sum7[21] +  root.sum7[23])/2,2),                          
                                 (sum(root.s97)+sum(root.s98))/2,   round((root.sum7[25] +  root.sum7[27])/2,2)] 
                  
                    
                for g in range(2):
                        root.stu7M[g +11].delete(0, tk.END)
                        root.stu7M[g +11].insert(0, root.sum7[g])
                        root.stu7M[g +25].delete(0, tk.END)
                        root.stu7M[g +25].insert(0, root.sum7[g+2])                    
                        root.stu7M[g +39].delete(0, tk.END)
                        root.stu7M[g +39].insert(0, root.TAVR7[g])            
                        root.stu7M[g +81].delete(0, tk.END)
                        root.stu7M[g +81].insert(0, root.TAVR7[g+2]) 
                        root.stu7M[g +123].delete(0, tk.END)
                        root.stu7M[g +123].insert(0, root.TAVR7[g+4])
                        root.stu7M[g +165].delete(0, tk.END)
                        root.stu7M[g +165].insert(0, root.TAVR7[g+6])
                        root.stu7M[g +207].delete(0, tk.END)
                        root.stu7M[g +207].insert(0, root.TAVR7[g+8])
                        root.stu7M[g +249].delete(0, tk.END)
                        root.stu7M[g +249].insert(0, root.TAVR7[g+10])
                        root.stu7M[g +291].delete(0, tk.END)
                        root.stu7M[g +291].insert(0, root.TAVR7[g+12])                                         
                        root.stu7M[g +53].delete(0, tk.END)
                        root.stu7M[g +53].insert(0, root.sum7[g+4])
                        root.stu7M[g +67].delete(0, tk.END)
                        root.stu7M[g +67].insert(0, root.sum7[g+6])
                        root.stu7M[g +95].delete(0, tk.END)
                        root.stu7M[g +95].insert(0, root.sum7[g+8])
                        root.stu7M[g +109].delete(0, tk.END)
                        root.stu7M[g +109].insert(0, root.sum7[g+10])
                        root.stu7M[g +137].delete(0, tk.END)
                        root.stu7M[g +137].insert(0, root.sum7[g+12])
                        root.stu7M[g +151].delete(0, tk.END)
                        root.stu7M[g +151].insert(0, root.sum7[g+14])
                        root.stu7M[g +179].delete(0, tk.END)
                        root.stu7M[g +179].insert(0, root.sum7[g+16])
                        root.stu7M[g +193].delete(0, tk.END)
                        root.stu7M[g +193].insert(0, root.sum7[g+18])
                        root.stu7M[g +221].delete(0, tk.END)
                        root.stu7M[g +221].insert(0, root.sum7[g+20])
                        root.stu7M[g +235].delete(0, tk.END)
                        root.stu7M[g +235].insert(0, root.sum7[g+22])
                        root.stu7M[g +263].delete(0, tk.END)
                        root.stu7M[g +263].insert(0, root.sum7[g+24])
                        root.stu7M[g +277].delete(0, tk.END)
                        root.stu7M[g +277].insert(0, root.sum7[g+26])
                
                
                # page8
                
                
                root.s99 = []  
                root.s100 = []
                    
                root.s101 = []  
                root.s102 = []            
                    
                root.s103 = []  
                root.s104 = []

                root.s105 = []  
                root.s106 = []
                    
                root.s107 = []  
                root.s108 = []
                    
                root.s109 = []  
                root.s110 = []
                    
                root.s111 = []  
                root.s112 = []
                    
                for B in range (11):
                        
                        x = (root.get_stu8()[B] + root.get_stu8()[B + 14]) / 2 
                        root.stu8M[B + 28].delete(0,tk.END)   
                        root.stu8M[B + 28].insert(0,x)     
                      
                                        
                        root.s99.append(root.get_stu8()[B])
                        root.s100.append(root.get_stu8()[B + 14])
                       
                        
                        y = (root.get_stu8()[B+ 42] + root.get_stu8()[B + 56]) / 2 
                        root.stu8M[B + 70].delete(0,tk.END)   
                        root.stu8M[B + 70].insert(0,y)
                        
                        root.s101.append(root.get_stu8()[B + 42])
                        root.s102.append(root.get_stu8()[B + 56])
                        
                        z = (root.get_stu8()[B+ 84] + root.get_stu8()[B + 98]) / 2 
                        root.stu8M[B + 112].delete(0,tk.END)   
                        root.stu8M[B + 112].insert(0,z)
                        
                        root.s103.append(root.get_stu8()[B+ 84])
                        root.s104.append(root.get_stu8()[B + 98])
                        
                        a = (root.get_stu8()[B+ 126] + root.get_stu8()[B + 140]) / 2 
                        root.stu8M[B + 154].delete(0,tk.END)   
                        root.stu8M[B + 154].insert(0,a)
                        
                        root.s105.append(root.get_stu8()[B+ 126])
                        root.s106.append(root.get_stu8()[B + 140])
                        
                        b = (root.get_stu8()[B+ 168] + root.get_stu8()[B + 182]) / 2 
                        root.stu8M[B + 196].delete(0,tk.END)   
                        root.stu8M[B + 196].insert(0,b)
                        
                        root.s107.append(root.get_stu8()[B + 168])
                        root.s108.append(root.get_stu8()[B + 182])
                        
                        c = (root.get_stu8()[B+ 210] + root.get_stu8()[B + 224]) / 2 
                        root.stu8M[B + 238].delete(0,tk.END)   
                        root.stu8M[B + 238].insert(0,c)
                        
                        root.s109.append(root.get_stu8()[B + 210])
                        root.s110.append(root.get_stu8()[B + 224])
                        
                        d = (root.get_stu8()[B+ 252] + root.get_stu8()[B + 266]) / 2 
                        root.stu8M[B + 280].delete(0,tk.END)   
                        root.stu8M[B + 280].insert(0,d)
                        
                        root.s111.append(root.get_stu8()[B + 252])
                        root.s112.append(root.get_stu8()[B + 266])
                        
                root.sum8 =    [ sum(root.s99),   round(sum(root.s99)/11,2),    sum(root.s100),  round(sum(root.s100)/11,2),
                                 sum(root.s101),  round(sum(root.s101)/11,2),   sum(root.s102),  round(sum(root.s102)/11,2),
                                 sum(root.s103),  round(sum(root.s103)/11,2),   sum(root.s104),  round(sum(root.s104)/11,2),
                                 sum(root.s105),  round(sum(root.s105)/11,2),   sum(root.s106),  round(sum(root.s106)/11,2),
                                 sum(root.s107),  round(sum(root.s107)/11,2),   sum(root.s108),  round(sum(root.s108)/11,2),
                                 sum(root.s109),  round(sum(root.s109)/11,2),   sum(root.s110),  round(sum(root.s110)/11,2),
                                 sum(root.s111),  round(sum(root.s111)/11,2),   sum(root.s112),  round(sum(root.s112)/11,2)] 
                                            
                root.TAVR8 =[    (sum(root.s99)+sum(root.s100))/2,    round((root.sum8[1]  +  root.sum8[3])/2,2), 
                                 (sum(root.s101)+sum(root.s102))/2,   round((root.sum8[5]  +  root.sum8[7])/2,2),                           
                                 (sum(root.s103)+sum(root.s104))/2,   round((root.sum8[9]  +  root.sum8[11])/2,2),  
                                 (sum(root.s105)+sum(root.s106))/2,   round((root.sum8[13] +  root.sum8[15])/2,2),                         
                                 (sum(root.s107)+sum(root.s108))/2,   round((root.sum8[17] +  root.sum8[19])/2,2), 
                                 (sum(root.s109)+sum(root.s110))/2,   round((root.sum8[21] +  root.sum8[23])/2,2),                          
                                 (sum(root.s111)+sum(root.s112))/2,   round((root.sum8[25] +  root.sum8[27])/2,2),] 
                  
                    
                for g in range(2):
                        root.stu8M[g +11].delete(0, tk.END)
                        root.stu8M[g +11].insert(0, root.sum8[g])
                        root.stu8M[g +25].delete(0, tk.END)
                        root.stu8M[g +25].insert(0, root.sum8[g+2])                    
                        root.stu8M[g +39].delete(0, tk.END)
                        root.stu8M[g +39].insert(0, root.TAVR8[g])            
                        root.stu8M[g +81].delete(0, tk.END)
                        root.stu8M[g +81].insert(0, root.TAVR8[g+2]) 
                        root.stu8M[g +123].delete(0, tk.END)
                        root.stu8M[g +123].insert(0, root.TAVR8[g+4])
                        root.stu8M[g +165].delete(0, tk.END)
                        root.stu8M[g +165].insert(0, root.TAVR8[g+6])
                        root.stu8M[g +207].delete(0, tk.END)
                        root.stu8M[g +207].insert(0, root.TAVR8[g+8])
                        root.stu8M[g +249].delete(0, tk.END)
                        root.stu8M[g +249].insert(0, root.TAVR8[g+10])
                        root.stu8M[g +291].delete(0, tk.END)
                        root.stu8M[g +291].insert(0, root.TAVR8[g+12])                                         
                        root.stu8M[g +53].delete(0, tk.END)
                        root.stu8M[g +53].insert(0, root.sum8[g+4])
                        root.stu8M[g +67].delete(0, tk.END)
                        root.stu8M[g +67].insert(0, root.sum8[g+6])
                        root.stu8M[g +95].delete(0, tk.END)
                        root.stu8M[g +95].insert(0, root.sum8[g+8])
                        root.stu8M[g +109].delete(0, tk.END)
                        root.stu8M[g +109].insert(0, root.sum8[g+10])
                        root.stu8M[g +137].delete(0, tk.END)
                        root.stu8M[g +137].insert(0, root.sum8[g+12])
                        root.stu8M[g +151].delete(0, tk.END)
                        root.stu8M[g +151].insert(0, root.sum8[g+14])
                        root.stu8M[g +179].delete(0, tk.END)
                        root.stu8M[g +179].insert(0, root.sum8[g+16])
                        root.stu8M[g +193].delete(0, tk.END)
                        root.stu8M[g +193].insert(0, root.sum8[g+18])
                        root.stu8M[g +221].delete(0, tk.END)
                        root.stu8M[g +221].insert(0, root.sum8[g+20])
                        root.stu8M[g +235].delete(0, tk.END)
                        root.stu8M[g +235].insert(0, root.sum8[g+22])
                        root.stu8M[g +263].delete(0, tk.END)
                        root.stu8M[g +263].insert(0, root.sum8[g+24])
                        root.stu8M[g +277].delete(0, tk.END)
                        root.stu8M[g +277].insert(0, root.sum8[g+26])
                
                # page9
                
                
                root.s113 = []  
                root.s114 = []
                    
                root.s115 = []  
                root.s116 = []            
                    
                root.s117 = []  
                root.s118 = []

                root.s119 = []  
                root.s120 = []
                    
                root.s121 = []  
                root.s122 = []
                    
                root.s123 = []  
                root.s124 = []
                    
                root.s125 = []  
                root.s126 = []
                    
                for B in range (11):
                        
                        x = (root.get_stu9()[B] + root.get_stu9()[B + 14]) / 2 
                        root.stu9M[B + 28].delete(0,tk.END)   
                        root.stu9M[B + 28].insert(0,x)     
                      
                                        
                        root.s113.append(root.get_stu9()[B])
                        root.s114.append(root.get_stu9()[B + 14])
                       
                        
                        y = (root.get_stu9()[B+ 42] + root.get_stu9()[B + 56]) / 2 
                        root.stu9M[B + 70].delete(0,tk.END)   
                        root.stu9M[B + 70].insert(0,y)
                        
                        root.s115.append(root.get_stu9()[B + 42])
                        root.s116.append(root.get_stu9()[B + 56])
                        
                        z = (root.get_stu9()[B+ 84] + root.get_stu9()[B + 98]) / 2 
                        root.stu9M[B + 112].delete(0,tk.END)   
                        root.stu9M[B + 112].insert(0,z)
                        
                        root.s117.append(root.get_stu9()[B+ 84])
                        root.s118.append(root.get_stu9()[B + 98])
                        
                        a = (root.get_stu9()[B+ 126] + root.get_stu9()[B + 140]) / 2 
                        root.stu9M[B + 154].delete(0,tk.END)   
                        root.stu9M[B + 154].insert(0,a)
                        
                        root.s119.append(root.get_stu9()[B+ 126])
                        root.s120.append(root.get_stu9()[B + 140])
                        
                        b = (root.get_stu9()[B+ 168] + root.get_stu9()[B + 182]) / 2 
                        root.stu9M[B + 196].delete(0,tk.END)   
                        root.stu9M[B + 196].insert(0,b)
                        
                        root.s121.append(root.get_stu9()[B + 168])
                        root.s122.append(root.get_stu9()[B + 182])
                        
                        c = (root.get_stu9()[B+ 210] + root.get_stu9()[B + 224]) / 2 
                        root.stu9M[B + 238].delete(0,tk.END)   
                        root.stu9M[B + 238].insert(0,c)
                        
                        root.s123.append(root.get_stu9()[B + 210])
                        root.s124.append(root.get_stu9()[B + 224])
                        
                        d = (root.get_stu9()[B+ 252] + root.get_stu9()[B + 266]) / 2 
                        root.stu9M[B + 280].delete(0,tk.END)   
                        root.stu9M[B + 280].insert(0,d)
                        
                        root.s125.append(root.get_stu9()[B + 252])
                        root.s126.append(root.get_stu9()[B + 266])
                        
                root.sum9 =    [ sum(root.s113),  round(sum(root.s113)/11,2),   sum(root.s114),  round(sum(root.s114)/11,2),
                                 sum(root.s115),  round(sum(root.s115)/11,2),   sum(root.s116),  round(sum(root.s116)/11,2),
                                 sum(root.s117),  round(sum(root.s117)/11,2),   sum(root.s118),  round(sum(root.s118)/11,2), 
                                 sum(root.s119),  round(sum(root.s119)/11,2),   sum(root.s120),  round(sum(root.s120)/11,2),
                                 sum(root.s121),  round(sum(root.s121)/11,2),   sum(root.s122),  round(sum(root.s122)/11,2),
                                 sum(root.s123),  round(sum(root.s123)/11,2),   sum(root.s124),  round(sum(root.s124)/11,2),
                                 sum(root.s125),  round(sum(root.s125)/11,2),   sum(root.s126),  round(sum(root.s126)/11,2)] 
                                            
                root.TAVR9 =[    (sum(root.s113)+sum(root.s114))/2,   round((root.sum9[1]  +  root.sum9[3])/2,2), 
                                 (sum(root.s115)+sum(root.s116))/2,   round((root.sum9[5]  +  root.sum9[7])/2,2),                           
                                 (sum(root.s117)+sum(root.s118))/2,   round((root.sum9[9]  +  root.sum9[11])/2,2),  
                                 (sum(root.s119)+sum(root.s120))/2,   round((root.sum9[13] +  root.sum9[15])/2,2),                        
                                 (sum(root.s121)+sum(root.s122))/2,   round((root.sum9[17] +  root.sum9[19])/2,2), 
                                 (sum(root.s123)+sum(root.s124))/2,   round((root.sum9[21] +  root.sum9[23])/2,2),                          
                                 (sum(root.s125)+sum(root.s126))/2,   round((root.sum9[25] +  root.sum9[27])/2,2)] 
                  
                    
                for g in range(2):
                        root.stu9M[g +11].delete(0, tk.END)
                        root.stu9M[g +11].insert(0, root.sum9[g])
                        root.stu9M[g +25].delete(0, tk.END)
                        root.stu9M[g +25].insert(0, root.sum9[g+2])                    
                        root.stu9M[g +39].delete(0, tk.END)
                        root.stu9M[g +39].insert(0, root.TAVR9[g])            
                        root.stu9M[g +81].delete(0, tk.END)
                        root.stu9M[g +81].insert(0, root.TAVR9[g+2]) 
                        root.stu9M[g +123].delete(0, tk.END)
                        root.stu9M[g +123].insert(0, root.TAVR9[g+4])
                        root.stu9M[g +165].delete(0, tk.END)
                        root.stu9M[g +165].insert(0, root.TAVR9[g+6])
                        root.stu9M[g +207].delete(0, tk.END)
                        root.stu9M[g +207].insert(0, root.TAVR9[g+8])
                        root.stu9M[g +249].delete(0, tk.END)
                        root.stu9M[g +249].insert(0, root.TAVR9[g+10])
                        root.stu9M[g +291].delete(0, tk.END)
                        root.stu9M[g +291].insert(0, root.TAVR9[g+12])                                         
                        root.stu9M[g +53].delete(0, tk.END)
                        root.stu9M[g +53].insert(0, root.sum9[g+4])
                        root.stu9M[g +67].delete(0, tk.END)
                        root.stu9M[g +67].insert(0, root.sum9[g+6])
                        root.stu9M[g +95].delete(0, tk.END)
                        root.stu9M[g +95].insert(0, root.sum9[g+8])
                        root.stu9M[g +109].delete(0, tk.END)
                        root.stu9M[g +109].insert(0, root.sum9[g+10])
                        root.stu9M[g +137].delete(0, tk.END)
                        root.stu9M[g +137].insert(0, root.sum9[g+12])
                        root.stu9M[g +151].delete(0, tk.END)
                        root.stu9M[g +151].insert(0, root.sum9[g+14])
                        root.stu9M[g +179].delete(0, tk.END)
                        root.stu9M[g +179].insert(0, root.sum9[g+16])
                        root.stu9M[g +193].delete(0, tk.END)
                        root.stu9M[g +193].insert(0, root.sum9[g+18])
                        root.stu9M[g +221].delete(0, tk.END)
                        root.stu9M[g +221].insert(0, root.sum9[g+20])
                        root.stu9M[g +235].delete(0, tk.END)
                        root.stu9M[g +235].insert(0, root.sum9[g+22])
                        root.stu9M[g +263].delete(0, tk.END)
                        root.stu9M[g +263].insert(0, root.sum9[g+24])
                        root.stu9M[g +277].delete(0, tk.END)
                        root.stu9M[g +277].insert(0, root.sum9[g+26])
                
                # page10
                
                
                root.s127 = []  
                root.s128 = []
                    
                root.s129 = []  
                root.s130 = []            
                    
                root.s131 = []  
                root.s132 = []

                root.s133 = []  
                root.s134 = []
                    
                root.s135 = []  
                root.s136 = []
                    
                root.s137 = []  
                root.s138 = []
                    
                root.s139 = []  
                root.s140 = []
                    
                for B in range (11):
                        
                        x = (root.get_stu10()[B] + root.get_stu10()[B + 14]) / 2 
                        root.stu10M[B + 28].delete(0,tk.END)   
                        root.stu10M[B + 28].insert(0,x)     
                      
                                        
                        root.s127.append(root.get_stu10()[B])
                        root.s128.append(root.get_stu10()[B + 14])
                       
                        
                        y = (root.get_stu10()[B+ 42] + root.get_stu10()[B + 56]) / 2 
                        root.stu10M[B + 70].delete(0,tk.END)   
                        root.stu10M[B + 70].insert(0,y)
                        
                        root.s129.append(root.get_stu10()[B + 42])
                        root.s130.append(root.get_stu10()[B + 56])
                        
                        z = (root.get_stu10()[B+ 84] + root.get_stu10()[B + 98]) / 2 
                        root.stu10M[B + 112].delete(0,tk.END)   
                        root.stu10M[B + 112].insert(0,z)
                        
                        root.s131.append(root.get_stu10()[B+ 84])
                        root.s132.append(root.get_stu10()[B + 98])
                        
                        a = (root.get_stu10()[B+ 126] + root.get_stu10()[B + 140]) / 2 
                        root.stu10M[B + 154].delete(0,tk.END)   
                        root.stu10M[B + 154].insert(0,a)
                        
                        root.s133.append(root.get_stu10()[B+ 126])
                        root.s134.append(root.get_stu10()[B + 140])
                        
                        b = (root.get_stu10()[B+ 168] + root.get_stu10()[B + 182]) / 2 
                        root.stu10M[B + 196].delete(0,tk.END)   
                        root.stu10M[B + 196].insert(0,b)
                        
                        root.s135.append(root.get_stu10()[B + 168])
                        root.s136.append(root.get_stu10()[B + 182])
                        
                        c = (root.get_stu10()[B+ 210] + root.get_stu10()[B + 224]) / 2 
                        root.stu10M[B + 238].delete(0,tk.END)   
                        root.stu10M[B + 238].insert(0,c)
                        
                        root.s137.append(root.get_stu10()[B + 210])
                        root.s138.append(root.get_stu10()[B + 224])
                        
                        d = (root.get_stu10()[B+ 252] + root.get_stu10()[B + 266]) / 2 
                        root.stu10M[B + 280].delete(0,tk.END)   
                        root.stu10M[B + 280].insert(0,d)
                        
                        root.s139.append(root.get_stu10()[B + 252])
                        root.s140.append(root.get_stu10()[B + 266])
                        
                root.sum10 =    [sum(root.s127),  round(sum(root.s127)/11,2),   sum(root.s128),  round(sum(root.s128)/11,2),
                                 sum(root.s129),  round(sum(root.s129)/11,2),   sum(root.s130),  round(sum(root.s130)/11,2),
                                 sum(root.s131),  round(sum(root.s131)/11,2),   sum(root.s132),  round(sum(root.s132)/11,2), 
                                 sum(root.s133),  round(sum(root.s133)/11,2),   sum(root.s134),  round(sum(root.s134)/11,2),
                                 sum(root.s135),  round(sum(root.s135)/11,2),   sum(root.s136),  round(sum(root.s136)/11,2),
                                 sum(root.s137),  round(sum(root.s137)/11,2),   sum(root.s138),  round(sum(root.s138)/11,2),
                                 sum(root.s139),  round(sum(root.s139)/11,2),   sum(root.s140),  round(sum(root.s140)/11,2)] 
                                            
                root.TAVR10 =[   (sum(root.s127)+sum(root.s128))/2,   round((root.sum10[1]  +  root.sum10[3])/2,2), 
                                 (sum(root.s129)+sum(root.s130))/2,   round((root.sum10[5]  +  root.sum10[7])/2,2),                           
                                 (sum(root.s131)+sum(root.s132))/2,   round((root.sum10[9]  +  root.sum10[11])/2,2),  
                                 (sum(root.s133)+sum(root.s134))/2,   round((root.sum10[13] +  root.sum10[15])/2,2),                         
                                 (sum(root.s135)+sum(root.s136))/2,   round((root.sum10[17] +  root.sum10[19])/2,2), 
                                 (sum(root.s137)+sum(root.s138))/2,   round((root.sum10[21] +  root.sum10[23])/2,2),                          
                                 (sum(root.s139)+sum(root.s140))/2,   round((root.sum10[25] +  root.sum10[27])/2,2)] 
                  
                    
                for g in range(2):
                        root.stu10M[g +11].delete(0, tk.END)
                        root.stu10M[g +11].insert(0, root.sum10[g])
                        root.stu10M[g +25].delete(0, tk.END)
                        root.stu10M[g +25].insert(0, root.sum10[g+2])                    
                        root.stu10M[g +39].delete(0, tk.END)
                        root.stu10M[g +39].insert(0, root.TAVR10[g])            
                        root.stu10M[g +81].delete(0, tk.END)
                        root.stu10M[g +81].insert(0, root.TAVR10[g+2]) 
                        root.stu10M[g +123].delete(0, tk.END)
                        root.stu10M[g +123].insert(0, root.TAVR10[g+4])
                        root.stu10M[g +165].delete(0, tk.END)
                        root.stu10M[g +165].insert(0, root.TAVR10[g+6])
                        root.stu10M[g +207].delete(0, tk.END)
                        root.stu10M[g +207].insert(0, root.TAVR10[g+8])
                        root.stu10M[g +249].delete(0, tk.END)
                        root.stu10M[g +249].insert(0, root.TAVR10[g+10])
                        root.stu10M[g +291].delete(0, tk.END)
                        root.stu10M[g +291].insert(0, root.TAVR10[g+12])                                         
                        root.stu10M[g +53].delete(0, tk.END)
                        root.stu10M[g +53].insert(0, root.sum10[g+4])
                        root.stu10M[g +67].delete(0, tk.END)
                        root.stu10M[g +67].insert(0, root.sum10[g+6])
                        root.stu10M[g +95].delete(0, tk.END)
                        root.stu10M[g +95].insert(0, root.sum10[g+8])
                        root.stu10M[g +109].delete(0, tk.END)
                        root.stu10M[g +109].insert(0, root.sum10[g+10])
                        root.stu10M[g +137].delete(0, tk.END)
                        root.stu10M[g +137].insert(0, root.sum10[g+12])
                        root.stu10M[g +151].delete(0, tk.END)
                        root.stu10M[g +151].insert(0, root.sum10[g+14])
                        root.stu10M[g +179].delete(0, tk.END)
                        root.stu10M[g +179].insert(0, root.sum10[g+16])
                        root.stu10M[g +193].delete(0, tk.END)
                        root.stu10M[g +193].insert(0, root.sum10[g+18])
                        root.stu10M[g +221].delete(0, tk.END)
                        root.stu10M[g +221].insert(0, root.sum10[g+20])
                        root.stu10M[g +235].delete(0, tk.END)
                        root.stu10M[g +235].insert(0, root.sum10[g+22])
                        root.stu10M[g +263].delete(0, tk.END)
                        root.stu10M[g +263].insert(0, root.sum10[g+24])
                        root.stu10M[g +277].delete(0, tk.END)
                        root.stu10M[g +277].insert(0, root.sum10[g+26])
                        
                                        # rank1 
                        
                        
                rank1 =  [sum(root.s1),sum(root.s3),  sum(root.s5),   sum(root.s7),sum(root.s9),
                         sum(root.s11),sum(root.s13), sum(root.s15), sum(root.s17),sum(root.s19),
                         sum(root.s21),sum(root.s23), sum(root.s25), sum(root.s27),sum(root.s29),      
                         sum(root.s31),sum(root.s33), sum(root.s35), sum(root.s37),sum(root.s39), 
                         sum(root.s41),sum(root.s43), sum(root.s45), sum(root.s47),sum(root.s49),
                         sum(root.s51),sum(root.s53), sum(root.s55), sum(root.s57),sum(root.s59),
                         sum(root.s61),sum(root.s63), sum(root.s65), sum(root.s67),sum(root.s69),
                         sum(root.s71),sum(root.s73), sum(root.s75), sum(root.s77),sum(root.s79),
                         sum(root.s81),sum(root.s83), sum(root.s85), sum(root.s87),sum(root.s89),
                         sum(root.s91),sum(root.s93), sum(root.s95), sum(root.s97),sum(root.s99),
                         sum(root.s101),sum(root.s103), sum(root.s105), sum(root.s107),sum(root.s109),
                         sum(root.s111),sum(root.s113), sum(root.s115), sum(root.s117),sum(root.s119),
                         sum(root.s121),sum(root.s123), sum(root.s125), sum(root.s127),sum(root.s129),
                         sum(root.s131),sum(root.s133), sum(root.s135), sum(root.s137),sum(root.s139), 
                         ]
                rank1.sort(reverse = True)
                   #page 1
                index = rank1.index(sum(root.s1))
                root.stu1M[13].delete(0, tk.END)
                root.stu1M[13].insert(0, index+1)
                
                index = rank1.index(sum(root.s3))
                root.stu1M[55].delete(0, tk.END)
                root.stu1M[55].insert(0, index+1)
                
                index = rank1.index(sum(root.s5))
                root.stu1M[97].delete(0, tk.END)
                root.stu1M[97].insert(0, index+1)
                
                index = rank1.index(sum(root.s7))
                root.stu1M[139].delete(0, tk.END)
                root.stu1M[139].insert(0, index+1)
                
                index = rank1.index(sum(root.s9))
                root.stu1M[181].delete(0, tk.END)
                root.stu1M[181].insert(0, index+1)
                
                index = rank1.index(sum(root.s11))
                root.stu1M[223].delete(0, tk.END)
                root.stu1M[223].insert(0, index+1)
                
                index = rank1.index(sum(root.s13))
                root.stu1M[265].delete(0, tk.END)
                root.stu1M[265].insert(0, index+1)
                
                                #page  2
                
                
                index = rank1.index(sum(root.s15))
                root.stu2M[13].delete(0, tk.END)
                root.stu2M[13].insert(0, index+1)
                
                index = rank1.index(sum(root.s17))
                root.stu2M[55].delete(0, tk.END)
                root.stu2M[55].insert(0, index+1)
                
                index = rank1.index(sum(root.s19))
                root.stu2M[97].delete(0, tk.END)
                root.stu2M[97].insert(0, index+1)
                
                index = rank1.index(sum(root.s21))
                root.stu2M[139].delete(0, tk.END)
                root.stu2M[139].insert(0, index+1)
                
                index = rank1.index(sum(root.s23))
                root.stu2M[181].delete(0, tk.END)
                root.stu2M[181].insert(0, index+1)
                
                index = rank1.index(sum(root.s25))
                root.stu2M[223].delete(0, tk.END)
                root.stu2M[223].insert(0, index+1)
                
                index = rank1.index(sum(root.s27))
                root.stu2M[265].delete(0, tk.END)
                root.stu2M[265].insert(0, index+1)
                
                        #page 3
                                        
                index = rank1.index(sum(root.s29))
                root.stu3M[13].delete(0, tk.END)
                root.stu3M[13].insert(0, index+1)
                
                index = rank1.index(sum(root.s31))
                root.stu3M[55].delete(0, tk.END)
                root.stu3M[55].insert(0, index+1)
                
                index = rank1.index(sum(root.s33))
                root.stu3M[97].delete(0, tk.END)
                root.stu3M[97].insert(0, index+1)
                
                index = rank1.index(sum(root.s35))
                root.stu3M[139].delete(0, tk.END)
                root.stu3M[139].insert(0, index+1)
                
                index = rank1.index(sum(root.s37))
                root.stu3M[181].delete(0, tk.END)
                root.stu3M[181].insert(0, index+1)
                
                index = rank1.index(sum(root.s39))
                root.stu3M[223].delete(0, tk.END)
                root.stu3M[223].insert(0, index+1)
                
                index = rank1.index(sum(root.s41))
                root.stu3M[265].delete(0, tk.END)
                root.stu3M[265].insert(0, index+1)
                
                        #page 4
                                        
                index = rank1.index(sum(root.s43))
                root.stu4M[13].delete(0, tk.END)
                root.stu4M[13].insert(0, index+1)
                
                index = rank1.index(sum(root.s45))
                root.stu4M[55].delete(0, tk.END)
                root.stu4M[55].insert(0, index+1)
                
                index = rank1.index(sum(root.s47))
                root.stu4M[97].delete(0, tk.END)
                root.stu4M[97].insert(0, index+1)
                
                index = rank1.index(sum(root.s49))
                root.stu4M[139].delete(0, tk.END)
                root.stu4M[139].insert(0, index+1)
                
                index = rank1.index(sum(root.s51))
                root.stu4M[181].delete(0, tk.END)
                root.stu4M[181].insert(0, index+1)
                
                index = rank1.index(sum(root.s53))
                root.stu4M[223].delete(0, tk.END)
                root.stu4M[223].insert(0, index+1)
                
                index = rank1.index(sum(root.s55))
                root.stu4M[265].delete(0, tk.END)
                root.stu4M[265].insert(0, index+1)
                
                             #page 5
                                        
                index = rank1.index(sum(root.s57))
                root.stu5M[13].delete(0, tk.END)
                root.stu5M[13].insert(0, index+1)
                
                index = rank1.index(sum(root.s59))
                root.stu5M[55].delete(0, tk.END)
                root.stu5M[55].insert(0, index+1)
                
                index = rank1.index(sum(root.s61))
                root.stu5M[97].delete(0, tk.END)
                root.stu5M[97].insert(0, index+1)
                
                index = rank1.index(sum(root.s63))
                root.stu5M[139].delete(0, tk.END)
                root.stu5M[139].insert(0, index+1)
                
                index = rank1.index(sum(root.s65))
                root.stu5M[181].delete(0, tk.END)
                root.stu5M[181].insert(0, index+1)
                
                index = rank1.index(sum(root.s67))
                root.stu5M[223].delete(0, tk.END)
                root.stu5M[223].insert(0, index+1)
                
                index = rank1.index(sum(root.s69))
                root.stu5M[265].delete(0, tk.END)
                root.stu5M[265].insert(0, index+1)
                
                        #page 6
                                        
                index = rank1.index(sum(root.s71))
                root.stu6M[13].delete(0, tk.END)
                root.stu6M[13].insert(0, index+1)
                
                index = rank1.index(sum(root.s73))
                root.stu6M[55].delete(0, tk.END)
                root.stu6M[55].insert(0, index+1)
                
                index = rank1.index(sum(root.s75))
                root.stu6M[97].delete(0, tk.END)
                root.stu6M[97].insert(0, index+1)
                
                index = rank1.index(sum(root.s77))
                root.stu6M[139].delete(0, tk.END)
                root.stu6M[139].insert(0, index+1)
                
                index = rank1.index(sum(root.s79))
                root.stu6M[181].delete(0, tk.END)
                root.stu6M[181].insert(0, index+1)
                
                index = rank1.index(sum(root.s81))
                root.stu6M[223].delete(0, tk.END)
                root.stu6M[223].insert(0, index+1)
                
                index = rank1.index(sum(root.s83))
                root.stu6M[265].delete(0, tk.END)
                root.stu6M[265].insert(0, index+1)
                
                
                        #page 7
                                        
                index = rank1.index(sum(root.s85))
                root.stu7M[13].delete(0, tk.END)
                root.stu7M[13].insert(0, index+1)
                
                index = rank1.index(sum(root.s87))
                root.stu7M[55].delete(0, tk.END)
                root.stu7M[55].insert(0, index+1)
                
                index = rank1.index(sum(root.s89))
                root.stu7M[97].delete(0, tk.END)
                root.stu7M[97].insert(0, index+1)
                
                index = rank1.index(sum(root.s91))
                root.stu7M[139].delete(0, tk.END)
                root.stu7M[139].insert(0, index+1)
                
                index = rank1.index(sum(root.s93))
                root.stu7M[181].delete(0, tk.END)
                root.stu7M[181].insert(0, index+1)
                
                index = rank1.index(sum(root.s95))
                root.stu7M[223].delete(0, tk.END)
                root.stu7M[223].insert(0, index+1)
                
                index = rank1.index(sum(root.s97))
                root.stu7M[265].delete(0, tk.END)
                root.stu7M[265].insert(0, index+1)
                
                
                        #page 8
                                        
                index = rank1.index(sum(root.s99))
                root.stu8M[13].delete(0, tk.END)
                root.stu8M[13].insert(0, index+1)
                
                index = rank1.index(sum(root.s101))
                root.stu8M[55].delete(0, tk.END)
                root.stu8M[55].insert(0, index+1)
                
                index = rank1.index(sum(root.s103))
                root.stu8M[97].delete(0, tk.END)
                root.stu8M[97].insert(0, index+1)
                
                index = rank1.index(sum(root.s105))
                root.stu8M[139].delete(0, tk.END)
                root.stu8M[139].insert(0, index+1)
                
                index = rank1.index(sum(root.s107))
                root.stu8M[181].delete(0, tk.END)
                root.stu8M[181].insert(0, index+1)
                
                index = rank1.index(sum(root.s109))
                root.stu8M[223].delete(0, tk.END)
                root.stu8M[223].insert(0, index+1)
                
                index = rank1.index(sum(root.s111))
                root.stu8M[265].delete(0, tk.END)
                root.stu8M[265].insert(0, index+1)
                
                        #page 9
                                        
                index = rank1.index(sum(root.s113))
                root.stu9M[13].delete(0, tk.END)
                root.stu9M[13].insert(0, index+1)
                
                index = rank1.index(sum(root.s115))
                root.stu9M[55].delete(0, tk.END)
                root.stu9M[55].insert(0, index+1)
                
                index = rank1.index(sum(root.s117))
                root.stu9M[97].delete(0, tk.END)
                root.stu9M[97].insert(0, index+1)
                
                index = rank1.index(sum(root.s119))
                root.stu9M[139].delete(0, tk.END)
                root.stu9M[139].insert(0, index+1)
                
                index = rank1.index(sum(root.s121))
                root.stu9M[181].delete(0, tk.END)
                root.stu9M[181].insert(0, index+1)
                
                index = rank1.index(sum(root.s123))
                root.stu9M[223].delete(0, tk.END)
                root.stu9M[223].insert(0, index+1)
                
                index = rank1.index(sum(root.s125))
                root.stu9M[265].delete(0, tk.END)
                root.stu9M[265].insert(0, index+1)
                
                
                        #page 10
                                        
                index = rank1.index(sum(root.s127))
                root.stu10M[13].delete(0, tk.END)
                root.stu10M[13].insert(0, index+1)
                
                index = rank1.index(sum(root.s129))
                root.stu10M[55].delete(0, tk.END)
                root.stu10M[55].insert(0, index+1)
                
                index = rank1.index(sum(root.s131))
                root.stu10M[97].delete(0, tk.END)
                root.stu10M[97].insert(0, index+1)
                
                index = rank1.index(sum(root.s133))
                root.stu10M[139].delete(0, tk.END)
                root.stu10M[139].insert(0, index+1)
                
                index = rank1.index(sum(root.s135))
                root.stu10M[181].delete(0, tk.END)
                root.stu10M[181].insert(0, index+1)
                
                index = rank1.index(sum(root.s137))
                root.stu10M[223].delete(0, tk.END)
                root.stu10M[223].insert(0, index+1)
                
                index = rank1.index(sum(root.s139))
                root.stu10M[265].delete(0, tk.END)
                root.stu10M[265].insert(0, index+1)
                
                                        #rank2
                
                
                rank2 = [sum(root.s2), sum(root.s4),  sum(root.s6),  sum(root.s8), sum(root.s10),
                         sum(root.s12),sum(root.s14), sum(root.s16), sum(root.s18),sum(root.s20),
                         sum(root.s22),sum(root.s24), sum(root.s26), sum(root.s28),sum(root.s30),      
                         sum(root.s32),sum(root.s34), sum(root.s36), sum(root.s38),sum(root.s40), 
                         sum(root.s42),sum(root.s44), sum(root.s46), sum(root.s48),sum(root.s50),
                         sum(root.s52),sum(root.s54), sum(root.s56), sum(root.s58),sum(root.s60),
                         sum(root.s62),sum(root.s64), sum(root.s66), sum(root.s68),sum(root.s70),
                         sum(root.s72),sum(root.s74), sum(root.s76), sum(root.s78),sum(root.s80),
                         sum(root.s82),sum(root.s84), sum(root.s86), sum(root.s88),sum(root.s90),
                         sum(root.s92),sum(root.s94), sum(root.s96), sum(root.s98),sum(root.s100),
                         sum(root.s102),sum(root.s104), sum(root.s106), sum(root.s108),sum(root.s110),
                         sum(root.s112),sum(root.s114), sum(root.s116), sum(root.s118),sum(root.s120),
                         sum(root.s122),sum(root.s124), sum(root.s126), sum(root.s128),sum(root.s130),
                         sum(root.s132),sum(root.s134), sum(root.s136), sum(root.s138),sum(root.s140), 
                         ]
                rank2.sort(reverse = True)
                
                        #page 1
                index = rank2.index(sum(root.s2))
                root.stu1M[27].delete(0, tk.END)
                root.stu1M[27].insert(0, index+1)
                
                index = rank2.index(sum(root.s4))
                root.stu1M[69].delete(0, tk.END)
                root.stu1M[69].insert(0, index+1)
                
                index = rank2.index(sum(root.s6))
                root.stu1M[111].delete(0, tk.END)
                root.stu1M[111].insert(0, index+1)
                
                index = rank2.index(sum(root.s8))
                root.stu1M[153].delete(0, tk.END)
                root.stu1M[153].insert(0, index+1)
                
                index = rank2.index(sum(root.s10))
                root.stu1M[195].delete(0, tk.END)
                root.stu1M[195].insert(0, index+1)
                
                index = rank2.index(sum(root.s12))
                root.stu1M[237].delete(0, tk.END)
                root.stu1M[237].insert(0, index+1)
                
                index = rank2.index(sum(root.s14))
                root.stu1M[279].delete(0, tk.END)
                root.stu1M[279].insert(0, index+1)
                
                        #page 2
                index = rank2.index(sum(root.s16))
                root.stu2M[27].delete(0, tk.END)
                root.stu2M[27].insert(0, index+1)
                
                index = rank2.index(sum(root.s18))
                root.stu2M[69].delete(0, tk.END)
                root.stu2M[69].insert(0, index+1)
                
                index = rank2.index(sum(root.s20))
                root.stu2M[111].delete(0, tk.END)
                root.stu2M[111].insert(0, index+1)
                
                index = rank2.index(sum(root.s22))
                root.stu2M[153].delete(0, tk.END)
                root.stu2M[153].insert(0, index+1)
                
                index = rank2.index(sum(root.s24))
                root.stu2M[195].delete(0, tk.END)
                root.stu2M[195].insert(0, index+1)
                
                index = rank2.index(sum(root.s26))
                root.stu2M[237].delete(0, tk.END)
                root.stu2M[237].insert(0, index+1)
                
                index = rank2.index(sum(root.s28))
                root.stu2M[279].delete(0, tk.END)
                root.stu2M[279].insert(0, index+1)
                
                             #page 3
                index = rank2.index(sum(root.s30))
                root.stu3M[27].delete(0, tk.END)
                root.stu3M[27].insert(0, index+1)
                
                index = rank2.index(sum(root.s32))
                root.stu3M[69].delete(0, tk.END)
                root.stu3M[69].insert(0, index+1)
                
                index = rank2.index(sum(root.s34))
                root.stu3M[111].delete(0, tk.END)
                root.stu3M[111].insert(0, index+1)
                
                index = rank2.index(sum(root.s36))
                root.stu3M[153].delete(0, tk.END)
                root.stu3M[153].insert(0, index+1)
                
                index = rank2.index(sum(root.s38))
                root.stu3M[195].delete(0, tk.END)
                root.stu3M[195].insert(0, index+1)
                
                index = rank2.index(sum(root.s40))
                root.stu3M[237].delete(0, tk.END)
                root.stu3M[237].insert(0, index+1)
                
                index = rank2.index(sum(root.s42))
                root.stu3M[279].delete(0, tk.END)
                root.stu3M[279].insert(0, index+1)
                
                        #page 4
                index = rank2.index(sum(root.s44))
                root.stu4M[27].delete(0, tk.END)
                root.stu4M[27].insert(0, index+1)
                
                index = rank2.index(sum(root.s46))
                root.stu4M[69].delete(0, tk.END)
                root.stu4M[69].insert(0, index+1)
                
                index = rank2.index(sum(root.s48))
                root.stu4M[111].delete(0, tk.END)
                root.stu4M[111].insert(0, index+1)
                
                index = rank2.index(sum(root.s50))
                root.stu4M[153].delete(0, tk.END)
                root.stu4M[153].insert(0, index+1)
                
                index = rank2.index(sum(root.s52))
                root.stu4M[195].delete(0, tk.END)
                root.stu4M[195].insert(0, index+1)
                
                index = rank2.index(sum(root.s54))
                root.stu4M[237].delete(0, tk.END)
                root.stu4M[237].insert(0, index+1)
                
                index = rank2.index(sum(root.s56))
                root.stu4M[279].delete(0, tk.END)
                root.stu4M[279].insert(0, index+1)
                
                        #page 5
                index = rank2.index(sum(root.s58))
                root.stu5M[27].delete(0, tk.END)
                root.stu5M[27].insert(0, index+1)
                
                index = rank2.index(sum(root.s60))
                root.stu5M[69].delete(0, tk.END)
                root.stu5M[69].insert(0, index+1)
                
                index = rank2.index(sum(root.s62))
                root.stu5M[111].delete(0, tk.END)
                root.stu5M[111].insert(0, index+1)
                
                index = rank2.index(sum(root.s64))
                root.stu5M[153].delete(0, tk.END)
                root.stu5M[153].insert(0, index+1)
                
                index = rank2.index(sum(root.s66))
                root.stu5M[195].delete(0, tk.END)
                root.stu5M[195].insert(0, index+1)
                
                index = rank2.index(sum(root.s68))
                root.stu5M[237].delete(0, tk.END)
                root.stu5M[237].insert(0, index+1)
                
                index = rank2.index(sum(root.s70))
                root.stu5M[279].delete(0, tk.END)
                root.stu5M[279].insert(0, index+1)
                
                        #page 6
                index = rank2.index(sum(root.s72))
                root.stu6M[27].delete(0, tk.END)
                root.stu6M[27].insert(0, index+1)
                
                index = rank2.index(sum(root.s74))
                root.stu6M[69].delete(0, tk.END)
                root.stu6M[69].insert(0, index+1)
                
                index = rank2.index(sum(root.s76))
                root.stu6M[111].delete(0, tk.END)
                root.stu6M[111].insert(0, index+1)
                
                index = rank2.index(sum(root.s78))
                root.stu6M[153].delete(0, tk.END)
                root.stu6M[153].insert(0, index+1)
                
                index = rank2.index(sum(root.s80))
                root.stu6M[195].delete(0, tk.END)
                root.stu6M[195].insert(0, index+1)
                
                index = rank2.index(sum(root.s82))
                root.stu6M[237].delete(0, tk.END)
                root.stu6M[237].insert(0, index+1)
                
                index = rank2.index(sum(root.s84))
                root.stu6M[279].delete(0, tk.END)
                root.stu6M[279].insert(0, index+1)
                
                        #page 7
                index = rank2.index(sum(root.s86))
                root.stu7M[27].delete(0, tk.END)
                root.stu7M[27].insert(0, index+1)
                
                index = rank2.index(sum(root.s88))
                root.stu7M[69].delete(0, tk.END)
                root.stu7M[69].insert(0, index+1)
                
                index = rank2.index(sum(root.s90))
                root.stu7M[111].delete(0, tk.END)
                root.stu7M[111].insert(0, index+1)
                
                index = rank2.index(sum(root.s92))
                root.stu7M[153].delete(0, tk.END)
                root.stu7M[153].insert(0, index+1)
                
                index = rank2.index(sum(root.s94))
                root.stu7M[195].delete(0, tk.END)
                root.stu7M[195].insert(0, index+1)
                
                index = rank2.index(sum(root.s96))
                root.stu7M[237].delete(0, tk.END)
                root.stu7M[237].insert(0, index+1)
                
                index = rank2.index(sum(root.s98))
                root.stu7M[279].delete(0, tk.END)
                root.stu7M[279].insert(0, index+1)
                
                        #page 8
                index = rank2.index(sum(root.s100))
                root.stu8M[27].delete(0, tk.END)
                root.stu8M[27].insert(0, index+1)
                
                index = rank2.index(sum(root.s102))
                root.stu8M[69].delete(0, tk.END)
                root.stu8M[69].insert(0, index+1)
                
                index = rank2.index(sum(root.s104))
                root.stu8M[111].delete(0, tk.END)
                root.stu8M[111].insert(0, index+1)
                
                index = rank2.index(sum(root.s106))
                root.stu8M[153].delete(0, tk.END)
                root.stu8M[153].insert(0, index+1)
                
                index = rank2.index(sum(root.s108))
                root.stu8M[195].delete(0, tk.END)
                root.stu8M[195].insert(0, index+1)
                
                index = rank2.index(sum(root.s110))
                root.stu8M[237].delete(0, tk.END)
                root.stu8M[237].insert(0, index+1)
                
                index = rank2.index(sum(root.s112))
                root.stu8M[279].delete(0, tk.END)
                root.stu8M[279].insert(0, index+1)
                
                        #page 9
                index = rank2.index(sum(root.s114))
                root.stu9M[27].delete(0, tk.END)
                root.stu9M[27].insert(0, index+1)
                
                index = rank2.index(sum(root.s116))
                root.stu9M[69].delete(0, tk.END)
                root.stu9M[69].insert(0, index+1)
                
                index = rank2.index(sum(root.s118))
                root.stu9M[111].delete(0, tk.END)
                root.stu9M[111].insert(0, index+1)
                
                index = rank2.index(sum(root.s120))
                root.stu9M[153].delete(0, tk.END)
                root.stu9M[153].insert(0, index+1)
                
                index = rank2.index(sum(root.s122))
                root.stu9M[195].delete(0, tk.END)
                root.stu9M[195].insert(0, index+1)
                
                index = rank2.index(sum(root.s124))
                root.stu9M[237].delete(0, tk.END)
                root.stu9M[237].insert(0, index+1)
                
                index = rank2.index(sum(root.s126))
                root.stu9M[279].delete(0, tk.END)
                root.stu9M[279].insert(0, index+1)
                
                        #page 10
                index = rank2.index(sum(root.s128))
                root.stu10M[27].delete(0, tk.END)
                root.stu10M[27].insert(0, index+1)
                
                index = rank2.index(sum(root.s130))
                root.stu10M[69].delete(0, tk.END)
                root.stu10M[69].insert(0, index+1)
                
                index = rank2.index(sum(root.s132))
                root.stu10M[111].delete(0, tk.END)
                root.stu10M[111].insert(0, index+1)
                
                index = rank2.index(sum(root.s134))
                root.stu10M[153].delete(0, tk.END)
                root.stu10M[153].insert(0, index+1)
                
                index = rank2.index(sum(root.s136))
                root.stu10M[195].delete(0, tk.END)
                root.stu10M[195].insert(0, index+1)
                
                index = rank2.index(sum(root.s138))
                root.stu10M[237].delete(0, tk.END)
                root.stu10M[237].insert(0, index+1)
                
                index = rank2.index(sum(root.s140))
                root.stu10M[279].delete(0, tk.END)
                root.stu10M[279].insert(0, index+1)
                
                        #rank3
                rank3 =    [sum(root.s1)+sum(root.s2)/2, sum(root.s3)+sum(root.s4)/2, sum(root.s5)+sum(root.s6)/2,
                           sum(root.s7)+sum(root.s8)/2, sum(root.s9)+sum(root.s10)/2, sum(root.s11)+sum(root.s12)/2,
                           sum(root.s13)+sum(root.s14)/2, sum(root.s15)+sum(root.s16)/2, sum(root.s17)+sum(root.s18)/2,
                           sum(root.s19)+sum(root.s20)/2, sum(root.s21)+sum(root.s22)/2, sum(root.s23)+sum(root.s24)/2,     
                           sum(root.s25)+sum(root.s26)/2, sum(root.s27)+sum(root.s28)/2, sum(root.s29)+sum(root.s30)/2,
                           sum(root.s31)+sum(root.s32)/2, sum(root.s33)+sum(root.s34)/2, sum(root.s35)+sum(root.s36)/2,
                           sum(root.s37)+sum(root.s38)/2, sum(root.s39)+sum(root.s40)/2, sum(root.s41)+sum(root.s42)/2,
                           sum(root.s43)+sum(root.s44)/2, sum(root.s45)+sum(root.s46)/2, sum(root.s47)+sum(root.s48)/2,
                           sum(root.s49)+sum(root.s50)/2, sum(root.s51)+sum(root.s52)/2, sum(root.s53)+sum(root.s54)/2,
                           sum(root.s55)+sum(root.s56)/2, sum(root.s57)+sum(root.s58)/2, sum(root.s59)+sum(root.s60)/2,
                           sum(root.s61)+sum(root.s62)/2, sum(root.s63)+sum(root.s64)/2, sum(root.s65)+sum(root.s66)/2,
                           sum(root.s67)+sum(root.s68)/2, sum(root.s69)+sum(root.s70)/2, sum(root.s71)+sum(root.s72)/2,
                           sum(root.s73)+sum(root.s74)/2, sum(root.s75)+sum(root.s76)/2, sum(root.s77)+sum(root.s78)/2,
                           sum(root.s79)+sum(root.s80)/2, sum(root.s81)+sum(root.s82)/2, sum(root.s83)+sum(root.s84)/2,
                           sum(root.s85)+sum(root.s86)/2, sum(root.s87)+sum(root.s88)/2, sum(root.s89)+sum(root.s90)/2,
                           sum(root.s91)+sum(root.s92)/2, sum(root.s93)+sum(root.s94)/2, sum(root.s95)+sum(root.s96)/2,
                           sum(root.s97)+sum(root.s98)/2, sum(root.s99)+sum(root.s100)/2, sum(root.s101)+sum(root.s102)/2,
                           sum(root.s103)+sum(root.s104)/2, sum(root.s105)+sum(root.s106)/2, sum(root.s107)+sum(root.s108)/2,
                           sum(root.s109)+sum(root.s110)/2, sum(root.s111)+sum(root.s112)/2, sum(root.s113)+sum(root.s114)/2,
                           sum(root.s115)+sum(root.s116)/2, sum(root.s117)+sum(root.s118)/2, sum(root.s119)+sum(root.s120)/2,
                           sum(root.s121)+sum(root.s122)/2, sum(root.s123)+sum(root.s124)/2, sum(root.s125)+sum(root.s126)/2,
                           sum(root.s127)+sum(root.s128)/2, sum(root.s129)+sum(root.s130)/2, sum(root.s131)+sum(root.s132)/2,
                           sum(root.s133)+sum(root.s134)/2, sum(root.s135)+sum(root.s136)/2, sum(root.s137)+sum(root.s138)/2,
                           sum(root.s139)+sum(root.s140)/2]
                
                rank3.sort(reverse = True)
                
                        #page 1
                index = rank3.index(sum(root.s1)+sum(root.s2)/2)
                root.stu1M[41].delete(0, tk.END)
                root.stu1M[41].insert(0, index+1)
                
                index = rank3.index(sum(root.s3)+sum(root.s4)/2)
                root.stu1M[83].delete(0, tk.END)
                root.stu1M[83].insert(0, index+1)
                
                index = rank3.index(sum(root.s5)+sum(root.s6)/2)
                root.stu1M[125].delete(0, tk.END)
                root.stu1M[125].insert(0, index+1)
                
                index = rank3.index(sum(root.s7)+sum(root.s8)/2)
                root.stu1M[167].delete(0, tk.END)
                root.stu1M[167].insert(0, index+1)
                
                index = rank3.index(sum(root.s9)+sum(root.s10)/2)
                root.stu1M[209].delete(0, tk.END)
                root.stu1M[209].insert(0, index+1)
                
                index = rank3.index(sum(root.s11)+sum(root.s12)/2)
                root.stu1M[251].delete(0, tk.END)
                root.stu1M[251].insert(0, index+1)
                
                index = rank3.index(sum(root.s13)+sum(root.s14)/2)
                root.stu1M[293].delete(0, tk.END)
                root.stu1M[293].insert(0, index+1)
        
        
                        #page 2
                        
                index = rank3.index(sum(root.s15)+sum(root.s16)/2)
                root.stu2M[41].delete(0, tk.END)
                root.stu2M[41].insert(0, index+1)
                
                index = rank3.index(sum(root.s17)+sum(root.s18)/2)
                root.stu2M[83].delete(0, tk.END)
                root.stu2M[83].insert(0, index+1)
                
                index = rank3.index(sum(root.s19)+sum(root.s20)/2)
                root.stu2M[125].delete(0, tk.END)
                root.stu2M[125].insert(0, index+1)
                
                index = rank3.index(sum(root.s21)+sum(root.s22)/2)
                root.stu2M[167].delete(0, tk.END)
                root.stu2M[167].insert(0, index+1)
                
                index = rank3.index(sum(root.s23)+sum(root.s24)/2)
                root.stu2M[209].delete(0, tk.END)
                root.stu2M[209].insert(0, index+1)
                
                index = rank3.index(sum(root.s25)+sum(root.s26)/2)
                root.stu2M[251].delete(0, tk.END)
                root.stu2M[251].insert(0, index+1)
                
                index = rank3.index(sum(root.s27)+sum(root.s28)/2)
                root.stu2M[293].delete(0, tk.END)
                root.stu2M[293].insert(0, index+1)
        
                        #page 3
                        
                index = rank3.index(sum(root.s29)+sum(root.s30)/2)
                root.stu3M[41].delete(0, tk.END)
                root.stu3M[41].insert(0, index+1)
                
                index = rank3.index(sum(root.s31)+sum(root.s32)/2)
                root.stu3M[83].delete(0, tk.END)
                root.stu3M[83].insert(0, index+1)
                
                index = rank3.index(sum(root.s33)+sum(root.s34)/2)
                root.stu3M[125].delete(0, tk.END)
                root.stu3M[125].insert(0, index+1)
                
                index = rank3.index(sum(root.s35)+sum(root.s36)/2)
                root.stu3M[167].delete(0, tk.END)
                root.stu3M[167].insert(0, index+1)
                
                index = rank3.index(sum(root.s37)+sum(root.s38)/2)
                root.stu3M[209].delete(0, tk.END)
                root.stu3M[209].insert(0, index+1)
                
                index = rank3.index(sum(root.s39)+sum(root.s40)/2)
                root.stu3M[251].delete(0, tk.END)
                root.stu3M[251].insert(0, index+1)
                
                index = rank3.index(sum(root.s41)+sum(root.s42)/2)
                root.stu3M[293].delete(0, tk.END)
                root.stu3M[293].insert(0, index+1)
        
                        #page 4
                        
                index = rank3.index(sum(root.s43)+sum(root.s44)/2)
                root.stu4M[41].delete(0, tk.END)
                root.stu4M[41].insert(0, index+1)
                
                index = rank3.index(sum(root.s45)+sum(root.s46)/2)
                root.stu4M[83].delete(0, tk.END)
                root.stu4M[83].insert(0, index+1)
                
                index = rank3.index(sum(root.s47)+sum(root.s48)/2)
                root.stu4M[125].delete(0, tk.END)
                root.stu4M[125].insert(0, index+1)
                
                index = rank3.index(sum(root.s49)+sum(root.s50)/2)
                root.stu4M[167].delete(0, tk.END)
                root.stu4M[167].insert(0, index+1)
                
                index = rank3.index(sum(root.s51)+sum(root.s52)/2)
                root.stu4M[209].delete(0, tk.END)
                root.stu4M[209].insert(0, index+1)
                
                index = rank3.index(sum(root.s53)+sum(root.s54)/2)
                root.stu4M[251].delete(0, tk.END)
                root.stu4M[251].insert(0, index+1)
                
                index = rank3.index(sum(root.s55)+sum(root.s56)/2)
                root.stu4M[293].delete(0, tk.END)
                root.stu4M[293].insert(0, index+1)
        
                               #page 5
                        
                index = rank3.index(sum(root.s57)+sum(root.s58)/2)
                root.stu5M[41].delete(0, tk.END)
                root.stu5M[41].insert(0, index+1)
                
                index = rank3.index(sum(root.s59)+sum(root.s60)/2)
                root.stu5M[83].delete(0, tk.END)
                root.stu5M[83].insert(0, index+1)
                
                index = rank3.index(sum(root.s61)+sum(root.s62)/2)
                root.stu5M[125].delete(0, tk.END)
                root.stu5M[125].insert(0, index+1)
                
                index = rank3.index(sum(root.s63)+sum(root.s64)/2)
                root.stu5M[167].delete(0, tk.END)
                root.stu5M[167].insert(0, index+1)
                
                index = rank3.index(sum(root.s65)+sum(root.s66)/2)
                root.stu5M[209].delete(0, tk.END)
                root.stu5M[209].insert(0, index+1)
                
                index = rank3.index(sum(root.s67)+sum(root.s68)/2)
                root.stu5M[251].delete(0, tk.END)
                root.stu5M[251].insert(0, index+1)
                
                index = rank3.index(sum(root.s69)+sum(root.s70)/2)
                root.stu5M[293].delete(0, tk.END)
                root.stu5M[293].insert(0, index+1)
                
                                #page 6
                        
                index = rank3.index(sum(root.s71)+sum(root.s72)/2)
                root.stu6M[41].delete(0, tk.END)
                root.stu6M[41].insert(0, index+1)
                
                index = rank3.index(sum(root.s73)+sum(root.s74)/2)
                root.stu6M[83].delete(0, tk.END)
                root.stu6M[83].insert(0, index+1)
                
                index = rank3.index(sum(root.s75)+sum(root.s76)/2)
                root.stu6M[125].delete(0, tk.END)
                root.stu6M[125].insert(0, index+1)
                
                index = rank3.index(sum(root.s77)+sum(root.s78)/2)
                root.stu6M[167].delete(0, tk.END)
                root.stu6M[167].insert(0, index+1)
                
                index = rank3.index(sum(root.s79)+sum(root.s80)/2)
                root.stu6M[209].delete(0, tk.END)
                root.stu6M[209].insert(0, index+1)
                
                index = rank3.index(sum(root.s81)+sum(root.s82)/2)
                root.stu6M[251].delete(0, tk.END)
                root.stu6M[251].insert(0, index+1)
                
                index = rank3.index(sum(root.s83)+sum(root.s84)/2)
                root.stu6M[293].delete(0, tk.END)
                root.stu6M[293].insert(0, index+1)
                
                                #page 7
                        
                index = rank3.index(sum(root.s85)+sum(root.s86)/2)
                root.stu7M[41].delete(0, tk.END)
                root.stu7M[41].insert(0, index+1)
                
                index = rank3.index(sum(root.s87)+sum(root.s88)/2)
                root.stu7M[83].delete(0, tk.END)
                root.stu7M[83].insert(0, index+1)
                
                index = rank3.index(sum(root.s89)+sum(root.s90)/2)
                root.stu7M[125].delete(0, tk.END)
                root.stu7M[125].insert(0, index+1)
                
                index = rank3.index(sum(root.s91)+sum(root.s92)/2)
                root.stu7M[167].delete(0, tk.END)
                root.stu7M[167].insert(0, index+1)
                
                index = rank3.index(sum(root.s93)+sum(root.s94)/2)
                root.stu7M[209].delete(0, tk.END)
                root.stu7M[209].insert(0, index+1)
                
                index = rank3.index(sum(root.s95)+sum(root.s96)/2)
                root.stu7M[251].delete(0, tk.END)
                root.stu7M[251].insert(0, index+1)
                
                index = rank3.index(sum(root.s97)+sum(root.s98)/2)
                root.stu7M[293].delete(0, tk.END)
                root.stu7M[293].insert(0, index+1)
                
                                #page 8
                        
                index = rank3.index(sum(root.s99)+sum(root.s100)/2)
                root.stu8M[41].delete(0, tk.END)
                root.stu8M[41].insert(0, index+1)
                
                index = rank3.index(sum(root.s101)+sum(root.s102)/2)
                root.stu8M[83].delete(0, tk.END)
                root.stu8M[83].insert(0, index+1)
                
                index = rank3.index(sum(root.s103)+sum(root.s104)/2)
                root.stu8M[125].delete(0, tk.END)
                root.stu8M[125].insert(0, index+1)
                
                index = rank3.index(sum(root.s105)+sum(root.s106)/2)
                root.stu8M[167].delete(0, tk.END)
                root.stu8M[167].insert(0, index+1)
                
                index = rank3.index(sum(root.s107)+sum(root.s108)/2)
                root.stu8M[209].delete(0, tk.END)
                root.stu8M[209].insert(0, index+1)
                
                index = rank3.index(sum(root.s109)+sum(root.s110)/2)
                root.stu8M[251].delete(0, tk.END)
                root.stu8M[251].insert(0, index+1)
                
                index = rank3.index(sum(root.s111)+sum(root.s112)/2)
                root.stu8M[293].delete(0, tk.END)
                root.stu8M[293].insert(0, index+1)
        
                                #page 9
                        
                index = rank3.index(sum(root.s113)+sum(root.s114)/2)
                root.stu9M[41].delete(0, tk.END)
                root.stu9M[41].insert(0, index+1)
                
                index = rank3.index(sum(root.s115)+sum(root.s116)/2)
                root.stu9M[83].delete(0, tk.END)
                root.stu9M[83].insert(0, index+1)
                
                index = rank3.index(sum(root.s117)+sum(root.s118)/2)
                root.stu9M[125].delete(0, tk.END)
                root.stu9M[125].insert(0, index+1)
                
                index = rank3.index(sum(root.s119)+sum(root.s120)/2)
                root.stu9M[167].delete(0, tk.END)
                root.stu9M[167].insert(0, index+1)
                
                index = rank3.index(sum(root.s121)+sum(root.s122)/2)
                root.stu9M[209].delete(0, tk.END)
                root.stu9M[209].insert(0, index+1)
                
                index = rank3.index(sum(root.s123)+sum(root.s124)/2)
                root.stu9M[251].delete(0, tk.END)
                root.stu9M[251].insert(0, index+1)
                
                index = rank3.index(sum(root.s125)+sum(root.s126)/2)
                root.stu9M[293].delete(0, tk.END)
                root.stu9M[293].insert(0, index+1)
                
                                #page 10
                        
                index = rank3.index(sum(root.s127)+sum(root.s128)/2)
                root.stu10M[41].delete(0, tk.END)
                root.stu10M[41].insert(0, index+1)
                
                index = rank3.index(sum(root.s129)+sum(root.s130)/2)
                root.stu10M[83].delete(0, tk.END)
                root.stu10M[83].insert(0, index+1)
                
                index = rank3.index(sum(root.s131)+sum(root.s132)/2)
                root.stu10M[125].delete(0, tk.END)
                root.stu10M[125].insert(0, index+1)
                
                index = rank3.index(sum(root.s133)+sum(root.s134)/2)
                root.stu10M[167].delete(0, tk.END)
                root.stu10M[167].insert(0, index+1)
                
                index = rank3.index(sum(root.s135)+sum(root.s136)/2)
                root.stu10M[209].delete(0, tk.END)
                root.stu10M[209].insert(0, index+1)
                
                index = rank3.index(sum(root.s137)+sum(root.s138)/2)
                root.stu10M[251].delete(0, tk.END)
                root.stu10M[251].insert(0, index+1)
                
                index = rank3.index(sum(root.s139)+sum(root.s140)/2)
                root.stu10M[293].delete(0, tk.END)
                root.stu10M[293].insert(0, index+1)
                
        def Add2(root):
        
            AM = [root.get_stu1()[0],root.get_stu1()[42],root.get_stu1()[84],root.get_stu1()[126],root.get_stu1()[168],root.get_stu1()[210],root.get_stu1()[252],
                  root.get_stu2()[0],root.get_stu2()[42],root.get_stu2()[84],root.get_stu2()[126],root.get_stu2()[168],root.get_stu2()[210],root.get_stu2()[252],
                  root.get_stu3()[0],root.get_stu3()[42],root.get_stu3()[84],root.get_stu3()[126],root.get_stu3()[168],root.get_stu3()[210],root.get_stu3()[252],
                  root.get_stu4()[0],root.get_stu4()[42],root.get_stu4()[84],root.get_stu4()[126],root.get_stu4()[168],root.get_stu4()[210],root.get_stu4()[252],
                  root.get_stu5()[0],root.get_stu5()[42],root.get_stu5()[84],root.get_stu5()[126],root.get_stu5()[168],root.get_stu5()[210],root.get_stu5()[252],
                  root.get_stu6()[0],root.get_stu6()[42],root.get_stu6()[84],root.get_stu6()[126],root.get_stu6()[168],root.get_stu6()[210],root.get_stu6()[252],
                  root.get_stu7()[0],root.get_stu7()[42],root.get_stu7()[84],root.get_stu7()[126],root.get_stu7()[168],root.get_stu7()[210],root.get_stu7()[252],
                  root.get_stu8()[0],root.get_stu8()[42],root.get_stu8()[84],root.get_stu8()[126],root.get_stu8()[168],root.get_stu8()[210],root.get_stu8()[252],
                  root.get_stu9()[0],root.get_stu9()[42],root.get_stu9()[84],root.get_stu9()[126],root.get_stu9()[168],root.get_stu9()[210],root.get_stu9()[252],
                  root.get_stu10()[0],root.get_stu10()[42],root.get_stu10()[84],root.get_stu10()[126],root.get_stu10()[168],root.get_stu10()[210],root.get_stu10()[252]]
           
            sex = [root.sex1.get(),root.sex2.get(),root.sex3.get(),root.sex4.get(),                    
                  root.sex5.get(),root.sex6.get(),root.sex7.get(),root.sex8.get(),
                  root.sex9.get(),root.sex10.get(),root.sex11.get(),root.sex12.get(),
                  root.sex13.get(),root.sex14.get(),root.sex15.get(),root.sex16.get(),
                  root.sex17.get(),root.sex18.get(),root.sex19.get(),root.sex20.get(),
                  root.sex21.get(),root.sex22.get(),root.sex23.get(),root.sex24.get(),
                  root.sex25.get(),root.sex26.get(),root.sex27.get(),root.sex28.get(),
                  root.sex29.get(),root.sex30.get(),root.sex31.get(),root.sex32.get(),
                  root.sex33.get(),root.sex34.get(),root.sex35.get(),root.sex36.get(),
                  root.sex37.get(),root.sex38.get(),root.sex39.get(),root.sex40.get(),
                  root.sex41.get(),root.sex42.get(),root.sex43.get(),root.sex44.get(),
                  root.sex45.get(),root.sex46.get(),root.sex47.get(),root.sex48.get(),
                  root.sex49.get(),root.sex50.get(),root.sex51.get(),root.sex52.get(),
                  root.sex53.get(),root.sex54.get(),root.sex55.get(),root.sex56.get(),
                  root.sex57.get(),root.sex58.get(),root.sex59.get(),root.sex60.get(),
                  root.sex61.get(),root.sex62.get(),root.sex63.get(),root.sex64.get(),
                  root.sex65.get(),root.sex66.get(),root.sex67.get(),root.sex68.get(),
                  root.sex69.get(),root.sex70.get()]
                                #Amharic
            
            count1 = 0
            for item in AM:
                        if 0 < item < 50:
                              count1 = count1+1
            root.num[0].delete(0, tk.END)
            root.num[0].insert(0, count1)         
            x1 = (count1 * float(root.per1.get())) / 100
            root.num[3].delete(0, tk.END)
            root.num[3].insert(0, x1) 
            
            count2 = 0
            for item in AM:
                     if item >= 50:
                         count2 = count2+1
            root.num[4].delete(0, tk.END)
            root.num[4].insert(0, count2)
            x2 = (count2 * float(root.per1.get())) / 100
            root.num[7].delete(0, tk.END)
            root.num[7].insert(0, x2) 
            
            count3 = 0
            for item in AM:
                     if item >= 75:
                         count3 = count3+1
            root.num[8].delete(0, tk.END)
            root.num[8].insert(0, count3)
            x3 = (count3 * float(root.per1.get())) / 100
            root.num[11].delete(0, tk.END)
            root.num[11].insert(0, x3) 
            
            count4 = 0
            for item in AM:
                     if item >= 85:
                         count4 = count4+1
            root.num[12].delete(0, tk.END)
            root.num[12].insert(0, count4)
            x4 = (count4 * float(root.per1.get())) / 100
            root.num[15].delete(0, tk.END)
            root.num[15].insert(0, x4)
            
            
            
            AM1 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and 0 < AM[q] <= 49:
                      AM1.append(q)
                  q=q+1
           
            root.num[1].delete(0, tk.END)
            root.num[1].insert(0, len(AM1))
            root.num[2].delete(0, tk.END)
            root.num[2].insert(0, count1 - len(AM1))

                 
            AM2 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and AM[q] >= 50:
                      AM2.append(q)
                  q=q+1
           
            root.num[5].delete(0, tk.END)
            root.num[5].insert(0, len(AM2))
            root.num[6].delete(0, tk.END)
            root.num[6].insert(0, count2 - len(AM2))     
                
            
            AM3 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and AM[q] >= 75:
                      AM3.append(q)
                  q=q+1
           
            root.num[9].delete(0, tk.END)
            root.num[9].insert(0, len(AM3))
            root.num[10].delete(0, tk.END)
            root.num[10].insert(0, count3 - len(AM3)) 
            
            AM4 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and AM[q] >= 85:
                      AM4.append(q)
                  q=q+1
           
            root.num[13].delete(0, tk.END)
            root.num[13].insert(0, len(AM4))
            root.num[14].delete(0, tk.END)
            root.num[14].insert(0, count4 - len(AM4)) 
            
            
            #ENGLISH
            
            EN = [root.get_stu1()[1],root.get_stu1()[43],root.get_stu1()[85],root.get_stu1()[127],root.get_stu1()[169],root.get_stu1()[211],root.get_stu1()[253],
                  root.get_stu2()[1],root.get_stu2()[43],root.get_stu2()[85],root.get_stu2()[127],root.get_stu2()[169],root.get_stu2()[211],root.get_stu2()[253],
                  root.get_stu3()[1],root.get_stu3()[43],root.get_stu3()[85],root.get_stu3()[127],root.get_stu3()[169],root.get_stu3()[211],root.get_stu3()[253],
                  root.get_stu4()[1],root.get_stu4()[43],root.get_stu4()[85],root.get_stu4()[127],root.get_stu4()[169],root.get_stu4()[211],root.get_stu4()[253],
                  root.get_stu5()[1],root.get_stu5()[43],root.get_stu5()[85],root.get_stu5()[127],root.get_stu5()[169],root.get_stu5()[211],root.get_stu5()[253],
                  root.get_stu6()[1],root.get_stu6()[43],root.get_stu6()[85],root.get_stu6()[127],root.get_stu6()[169],root.get_stu6()[211],root.get_stu6()[253],
                  root.get_stu7()[1],root.get_stu7()[43],root.get_stu7()[85],root.get_stu7()[127],root.get_stu7()[169],root.get_stu7()[211],root.get_stu7()[253],
                  root.get_stu8()[1],root.get_stu8()[43],root.get_stu8()[85],root.get_stu8()[127],root.get_stu8()[169],root.get_stu8()[211],root.get_stu8()[253],
                  root.get_stu9()[1],root.get_stu9()[43],root.get_stu9()[85],root.get_stu9()[127],root.get_stu9()[169],root.get_stu9()[211],root.get_stu9()[253],
                  root.get_stu10()[1],root.get_stu10()[43],root.get_stu10()[85],root.get_stu10()[127],root.get_stu10()[169],root.get_stu10()[211],root.get_stu10()[253]]
            EN1 = 0
            for item in EN:
                        if 0 < item < 50:
                              EN1 = EN1+1
            root.num[16].delete(0, tk.END)
            root.num[16].insert(0, EN1) 
            x5 = (EN1 * float(root.per1.get())) / 100
            root.num[19].delete(0, tk.END)
            root.num[19].insert(0, x5)
            
            
            
            EN2 = 0
            for item in EN:
                     if item >= 50:
                         EN2 = EN2+1
            root.num[20].delete(0, tk.END)
            root.num[20].insert(0, EN2)
            x6 = (EN2 * float(root.per1.get())) / 100
            root.num[23].delete(0, tk.END)
            root.num[23].insert(0, x6)
            
            EN3 = 0
            for item in EN:
                     if item >= 75:
                         EN3 = EN3+1
            root.num[24].delete(0, tk.END)
            root.num[24].insert(0,EN3)
            x7 = (EN3 * float(root.per1.get())) / 100
            root.num[27].delete(0, tk.END)
            root.num[27].insert(0, x7)
            
            EN4 = 0
            for item in EN:
                     if item >= 85:
                         EN4 = EN4+1
            root.num[28].delete(0, tk.END)
            root.num[28].insert(0, EN4)
            x8 = (EN3 * float(root.per1.get())) / 100
            root.num[31].delete(0, tk.END)
            root.num[31].insert(0, x8)
            
            E1 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and 0 < EN[q] <= 49:
                      E1.append(q)
                  q=q+1
           
            root.num[17].delete(0, tk.END)
            root.num[17].insert(0, len(E1))
            root.num[18].delete(0, tk.END)
            root.num[18].insert(0, EN1 - len(E1))
            
            E2 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and EN[q] >= 50:
                      E2.append(q)
                  q=q+1
           
            root.num[21].delete(0, tk.END)
            root.num[21].insert(0, len(E2))
            root.num[22].delete(0, tk.END)
            root.num[22].insert(0, EN2 - len(E2))  
            
            E3 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and EN[q] >= 75:
                      E3.append(q)
                  q=q+1
           
            root.num[25].delete(0, tk.END)
            root.num[25].insert(0, len(E3))
            root.num[26].delete(0, tk.END)
            root.num[26].insert(0, EN3 - len(E3))
            
            
            E4 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and EN[q] >= 85:
                      E4.append(q)
                  q=q+1
           
            root.num[29].delete(0, tk.END)
            root.num[29].insert(0, len(E4))
            root.num[30].delete(0, tk.END)
            root.num[30].insert(0, EN4 - len(E4))
            
            #MATHES
            
            MA = [root.get_stu1()[2],root.get_stu1()[44],root.get_stu1()[86],root.get_stu1()[128],root.get_stu1()[170],root.get_stu1()[212],root.get_stu1()[254],
                  root.get_stu2()[2],root.get_stu2()[44],root.get_stu2()[86],root.get_stu2()[128],root.get_stu2()[170],root.get_stu2()[212],root.get_stu2()[254],
                  root.get_stu3()[2],root.get_stu3()[44],root.get_stu3()[86],root.get_stu3()[128],root.get_stu3()[170],root.get_stu3()[212],root.get_stu3()[254],
                  root.get_stu4()[2],root.get_stu4()[44],root.get_stu4()[86],root.get_stu4()[128],root.get_stu4()[170],root.get_stu4()[212],root.get_stu4()[254],
                  root.get_stu5()[2],root.get_stu5()[44],root.get_stu5()[86],root.get_stu5()[128],root.get_stu5()[170],root.get_stu5()[212],root.get_stu5()[254],
                  root.get_stu6()[2],root.get_stu6()[44],root.get_stu6()[86],root.get_stu6()[128],root.get_stu6()[170],root.get_stu6()[212],root.get_stu6()[254],
                  root.get_stu7()[2],root.get_stu7()[44],root.get_stu7()[86],root.get_stu7()[128],root.get_stu7()[170],root.get_stu7()[212],root.get_stu7()[254],
                  root.get_stu8()[2],root.get_stu8()[44],root.get_stu8()[86],root.get_stu8()[128],root.get_stu8()[170],root.get_stu8()[212],root.get_stu8()[254],
                  root.get_stu9()[2],root.get_stu9()[44],root.get_stu9()[86],root.get_stu9()[128],root.get_stu9()[170],root.get_stu9()[212],root.get_stu9()[254],
                  root.get_stu10()[2],root.get_stu10()[44],root.get_stu10()[86],root.get_stu10()[128],root.get_stu10()[170],root.get_stu10()[212],root.get_stu10()[254]] 
            
            MA1 = 0
            for item in MA:
                        if 0 < item < 50:
                              MA1 = MA1+1
            root.num[32].delete(0, tk.END)
            root.num[32].insert(0, MA1) 
            x9 = (MA1 * float(root.per1.get())) / 100
            root.num[35].delete(0, tk.END)
            root.num[35].insert(0, x9)
            
            MA2 = 0
            for item in MA:
                     if item >= 50:
                         MA2 = MA2+1
            root.num[36].delete(0, tk.END)
            root.num[36].insert(0, MA2)
            x10 = (MA2 * float(root.per1.get())) / 100
            root.num[39].delete(0, tk.END)
            root.num[39].insert(0, x10)
            
            MA3 = 0
            for item in MA:
                     if item >= 75:
                         MA3 = MA3+1
            root.num[40].delete(0, tk.END)
            root.num[40].insert(0,MA3)
            x11 = (MA3 * float(root.per1.get())) / 100
            root.num[43].delete(0, tk.END)
            root.num[43].insert(0, x11)
            
            MA4 = 0
            for item in MA:
                     if item >= 85:
                         MA4 = MA4+1
            root.num[44].delete(0, tk.END)
            root.num[44].insert(0, MA4)
            x12 = (MA4 * float(root.per1.get())) / 100
            root.num[47].delete(0, tk.END)
            root.num[47].insert(0, x12)
            
            M1 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and 0 < MA[q] <= 49:
                      M1.append(q)
                  q=q+1
           
            root.num[33].delete(0, tk.END)
            root.num[33].insert(0, len(M1))
            root.num[34].delete(0, tk.END)
            root.num[34].insert(0, MA1 - len(M1))
            
            M2 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and MA[q] >= 50:
                      M2.append(q)
                  q=q+1
           
            root.num[37].delete(0, tk.END)
            root.num[37].insert(0, len(M2))
            root.num[38].delete(0, tk.END)
            root.num[38].insert(0, MA2 - len(M2))  
            
            M3 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and MA[q] >= 75:
                      M3.append(q)
                  q=q+1
           
            root.num[41].delete(0, tk.END)
            root.num[41].insert(0, len(M3))
            root.num[42].delete(0, tk.END)
            root.num[42].insert(0, MA3 - len(M3))
            
            M4 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and MA[q] >= 85:
                      M4.append(q)
                  q=q+1
           
            root.num[45].delete(0, tk.END)
            root.num[45].insert(0, len(M4))
            root.num[46].delete(0, tk.END)
            root.num[46].insert(0, MA4 - len(M4))
            
            #PYHISICS
            
            ph = [root.get_stu1()[3],root.get_stu1()[45],root.get_stu1()[87],root.get_stu1()[129],root.get_stu1()[171],root.get_stu1()[213],root.get_stu1()[255],
                  root.get_stu2()[3],root.get_stu2()[45],root.get_stu2()[87],root.get_stu2()[129],root.get_stu2()[171],root.get_stu2()[213],root.get_stu2()[255],
                  root.get_stu3()[3],root.get_stu3()[45],root.get_stu3()[87],root.get_stu3()[129],root.get_stu3()[171],root.get_stu3()[213],root.get_stu3()[255],
                  root.get_stu4()[3],root.get_stu4()[45],root.get_stu4()[87],root.get_stu4()[129],root.get_stu4()[171],root.get_stu4()[213],root.get_stu4()[255],
                  root.get_stu5()[3],root.get_stu5()[45],root.get_stu5()[87],root.get_stu5()[129],root.get_stu5()[171],root.get_stu5()[213],root.get_stu5()[255],
                  root.get_stu6()[3],root.get_stu6()[45],root.get_stu6()[87],root.get_stu6()[129],root.get_stu6()[171],root.get_stu6()[213],root.get_stu6()[255],
                  root.get_stu7()[3],root.get_stu7()[45],root.get_stu7()[87],root.get_stu7()[129],root.get_stu7()[171],root.get_stu7()[213],root.get_stu7()[255],
                  root.get_stu8()[3],root.get_stu8()[45],root.get_stu8()[87],root.get_stu8()[129],root.get_stu8()[171],root.get_stu8()[213],root.get_stu8()[255],
                  root.get_stu9()[3],root.get_stu9()[45],root.get_stu9()[87],root.get_stu9()[129],root.get_stu9()[171],root.get_stu9()[213],root.get_stu9()[255],
                  root.get_stu10()[3],root.get_stu10()[45],root.get_stu10()[87],root.get_stu10()[129],root.get_stu10()[171],root.get_stu10()[213],root.get_stu10()[255]]
            PH1 = 0
            for item in ph:
                        if 0 < item < 50:
                              PH1 = PH1+1
            root.num[48].delete(0, tk.END)
            root.num[48].insert(0, PH1)
            x13 = (PH1 * float(root.per1.get())) / 100
            root.num[51].delete(0, tk.END)
            root.num[51].insert(0, x13)            
            
            PH2 = 0
            for item in ph:
                     if item >= 50:
                         PH2 = PH2+1
            root.num[52].delete(0, tk.END)
            root.num[52].insert(0, PH2)
            x14 = (PH2 * float(root.per1.get())) / 100
            root.num[55].delete(0, tk.END)
            root.num[55].insert(0, x14)
            
            PH3 = 0
            for item in ph:
                     if item >= 75:
                         PH3 = PH3+1
            root.num[56].delete(0, tk.END)
            root.num[56].insert(0, PH3)
            x15 = (PH3 * float(root.per1.get())) / 100
            root.num[59].delete(0, tk.END)
            root.num[59].insert(0, x15)
            
            
            PH4 = 0
            for item in ph:
                     if item >= 85:
                         PH4 = PH4+1
            root.num[60].delete(0, tk.END)
            root.num[60].insert(0, PH4)
            x16 = (PH4 * float(root.per1.get())) / 100
            root.num[63].delete(0, tk.END)
            root.num[63].insert(0, x16)
            
            p1 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and 0 < ph[q] <= 49:
                      p1.append(q)
                  q=q+1
           
            root.num[49].delete(0, tk.END)
            root.num[49].insert(0, len(p1))
            root.num[50].delete(0, tk.END)
            root.num[50].insert(0, PH1 - len(p1))
            
            p2 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and ph[q] >= 50:
                      p2.append(q)
                  q=q+1
           
            root.num[53].delete(0, tk.END)
            root.num[53].insert(0, len(p2))
            root.num[54].delete(0, tk.END)
            root.num[54].insert(0, PH2 - len(p2))
            
            p3 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and ph[q] >= 75:
                      p3.append(q)
                  q=q+1
           
            root.num[57].delete(0, tk.END)
            root.num[57].insert(0, len(p3))
            root.num[58].delete(0, tk.END)
            root.num[58].insert(0, PH3 - len(p3))
            
            p4 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and ph[q] >= 85:
                      p4.append(q)
                  q=q+1
           
            root.num[61].delete(0, tk.END)
            root.num[61].insert(0, len(p4))
            root.num[62].delete(0, tk.END)
            root.num[62].insert(0, PH4 - len(p4))
            

            #CHEMISTRY
            
            ch = [root.get_stu1()[4],root.get_stu1()[46],root.get_stu1()[88],root.get_stu1()[130],root.get_stu1()[172],root.get_stu1()[214],root.get_stu1()[256],
                  root.get_stu2()[4],root.get_stu2()[46],root.get_stu2()[88],root.get_stu2()[130],root.get_stu2()[172],root.get_stu2()[214],root.get_stu2()[256],
                  root.get_stu3()[4],root.get_stu3()[46],root.get_stu3()[88],root.get_stu3()[130],root.get_stu3()[172],root.get_stu3()[214],root.get_stu3()[256],
                  root.get_stu4()[4],root.get_stu4()[46],root.get_stu4()[88],root.get_stu4()[130],root.get_stu4()[172],root.get_stu4()[214],root.get_stu4()[256],
                  root.get_stu5()[4],root.get_stu5()[46],root.get_stu5()[88],root.get_stu5()[130],root.get_stu5()[172],root.get_stu5()[214],root.get_stu5()[256],
                  root.get_stu6()[4],root.get_stu6()[46],root.get_stu6()[88],root.get_stu6()[130],root.get_stu6()[172],root.get_stu6()[214],root.get_stu6()[256],
                  root.get_stu7()[4],root.get_stu7()[46],root.get_stu7()[88],root.get_stu7()[130],root.get_stu7()[172],root.get_stu7()[214],root.get_stu7()[256],
                  root.get_stu8()[4],root.get_stu8()[46],root.get_stu8()[88],root.get_stu8()[130],root.get_stu8()[172],root.get_stu8()[214],root.get_stu8()[256],
                  root.get_stu9()[4],root.get_stu9()[46],root.get_stu9()[88],root.get_stu9()[130],root.get_stu9()[172],root.get_stu9()[214],root.get_stu9()[256],
                  root.get_stu10()[4],root.get_stu10()[46],root.get_stu10()[88],root.get_stu10()[130],root.get_stu10()[172],root.get_stu10()[214],root.get_stu10()[256]]             
            CH1 = 0
            for item in ch:
                        if 0 < item < 50:
                              CH1 = CH1+1
            root.num[64].delete(0, tk.END)
            root.num[64].insert(0, CH1)
            x17 = (CH1 * float(root.per1.get())) / 100
            root.num[67].delete(0, tk.END)
            root.num[67].insert(0, x17)
            
            CH2 = 0
            for item in ch:
                        if item >= 50:
                              CH2 = CH2+1
            root.num[68].delete(0, tk.END)
            root.num[68].insert(0, CH2)
            x18 = (CH2 * float(root.per1.get())) / 100
            root.num[71].delete(0, tk.END)
            root.num[71].insert(0, x18)
            
            CH3 = 0
            for item in ch:
                        if item >= 75:
                              CH3 = CH3+1
            root.num[72].delete(0, tk.END)
            root.num[72].insert(0, CH3)
            x19 = (CH3 * float(root.per1.get())) / 100
            root.num[75].delete(0, tk.END)
            root.num[75].insert(0, x19)
            
            CH4 = 0
            for item in ch:
                        if item >= 85:
                              CH4 = CH4+1
            root.num[76].delete(0, tk.END)
            root.num[76].insert(0, CH4)
            x20 = (CH4 * float(root.per1.get())) / 100
            root.num[79].delete(0, tk.END)
            root.num[79].insert(0, x20)
            
            C1 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and 0 < ch[q] <= 49:
                      C1.append(q)
                  q=q+1
           
            root.num[65].delete(0, tk.END)
            root.num[65].insert(0, len(C1))
            root.num[66].delete(0, tk.END)
            root.num[66].insert(0, CH1 - len(C1))
            
            C2 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  ch[q] >= 50:
                      C2.append(q)
                  q=q+1
           
            root.num[69].delete(0, tk.END)
            root.num[69].insert(0, len(C2))
            root.num[70].delete(0, tk.END)
            root.num[70].insert(0, CH2 - len(C2))
            
            
            C3 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  ch[q] >= 75:
                      C3.append(q)
                  q=q+1
           
            root.num[73].delete(0, tk.END)
            root.num[73].insert(0, len(C3))
            root.num[74].delete(0, tk.END)
            root.num[74].insert(0, CH3 - len(C3))
            
            C4 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  ch[q] >= 85:
                      C4.append(q)
                  q=q+1
           
            root.num[77].delete(0, tk.END)
            root.num[77].insert(0, len(C4))
            root.num[78].delete(0, tk.END)
            root.num[78].insert(0, CH4 - len(C4))
            
            
            #BIOLOGY
            
            bi = [root.get_stu1()[5],root.get_stu1()[47],root.get_stu1()[89],root.get_stu1()[131],root.get_stu1()[173],root.get_stu1()[215],root.get_stu1()[257],
                  root.get_stu2()[5],root.get_stu2()[47],root.get_stu2()[89],root.get_stu2()[131],root.get_stu2()[173],root.get_stu2()[215],root.get_stu2()[257],
                  root.get_stu3()[5],root.get_stu3()[47],root.get_stu3()[89],root.get_stu3()[131],root.get_stu3()[173],root.get_stu3()[215],root.get_stu3()[257],
                  root.get_stu4()[5],root.get_stu4()[47],root.get_stu4()[89],root.get_stu4()[131],root.get_stu4()[173],root.get_stu4()[215],root.get_stu4()[257],
                  root.get_stu5()[5],root.get_stu5()[47],root.get_stu5()[89],root.get_stu5()[131],root.get_stu5()[173],root.get_stu5()[215],root.get_stu5()[257],
                  root.get_stu6()[5],root.get_stu6()[47],root.get_stu6()[89],root.get_stu6()[131],root.get_stu6()[173],root.get_stu6()[215],root.get_stu6()[257],
                  root.get_stu7()[5],root.get_stu7()[47],root.get_stu7()[89],root.get_stu7()[131],root.get_stu7()[173],root.get_stu7()[215],root.get_stu7()[257],
                  root.get_stu8()[5],root.get_stu8()[47],root.get_stu8()[89],root.get_stu8()[131],root.get_stu8()[173],root.get_stu8()[215],root.get_stu8()[257],
                  root.get_stu9()[5],root.get_stu9()[47],root.get_stu9()[89],root.get_stu9()[131],root.get_stu9()[173],root.get_stu9()[215],root.get_stu9()[257],
                  root.get_stu10()[5],root.get_stu10()[47],root.get_stu10()[89],root.get_stu10()[131],root.get_stu10()[173],root.get_stu10()[215],root.get_stu10()[257]]
            BI1 = 0
            for item in bi:
                        if 0 < item < 50:
                              BI1 = BI1+1
            root.num[80].delete(0, tk.END)
            root.num[80].insert(0, BI1)
            x21 = (BI1 * float(root.per1.get())) / 100
            root.num[83].delete(0, tk.END)
            root.num[83].insert(0, x21)
            
            BI2 = 0
            for item in bi:
                        if item >= 50:
                              BI2 = BI2+1
            root.num[84].delete(0, tk.END)
            root.num[84].insert(0, BI2)
            x22 = (BI2 * float(root.per1.get())) / 100
            root.num[87].delete(0, tk.END)
            root.num[87].insert(0, x22)
            
            BI3 = 0
            for item in bi:
                        if item >= 75:
                              BI3 = BI3+1
            root.num[88].delete(0, tk.END)
            root.num[88].insert(0, BI3)
            x23 = (BI3 * float(root.per1.get())) / 100
            root.num[91].delete(0, tk.END)
            root.num[91].insert(0, x23)
            
            BI4 = 0
            for item in bi:
                        if item >= 85:
                              BI4 = BI4+1
            root.num[92].delete(0, tk.END)
            root.num[92].insert(0, BI4)
            x24 = (BI4 * float(root.per1.get())) / 100
            root.num[95].delete(0, tk.END)
            root.num[95].insert(0, x24)
            
            B1 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and 0 < bi[q] <= 49:
                      B1.append(q)
                  q=q+1
           
            root.num[81].delete(0, tk.END)
            root.num[81].insert(0, len(B1))
            root.num[82].delete(0, tk.END)
            root.num[82].insert(0, BI1 - len(B1))
            
            
            B2 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  bi[q] >= 50:
                      B2.append(q)
                  q=q+1
           
            root.num[85].delete(0, tk.END)
            root.num[85].insert(0, len(B2))
            root.num[86].delete(0, tk.END)
            root.num[86].insert(0, BI2 - len(B2))
            
            B3 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  bi[q] >= 75:
                      B3.append(q)
                  q=q+1
           
            root.num[89].delete(0, tk.END)
            root.num[89].insert(0, len(B3))
            root.num[90].delete(0, tk.END)
            root.num[90].insert(0, BI3 - len(B3))
            
            B4 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  bi[q] >= 85:
                      B4.append(q)
                  q=q+1
           
            root.num[93].delete(0, tk.END)
            root.num[93].insert(0, len(B4))
            root.num[94].delete(0, tk.END)
            root.num[94].insert(0, BI4 - len(B4))
            
            #GEOGRAPHY
            
            gi = [root.get_stu1()[6],root.get_stu1()[48],root.get_stu1()[90],root.get_stu1()[132],root.get_stu1()[174],root.get_stu1()[216],root.get_stu1()[258],
                  root.get_stu2()[6],root.get_stu2()[48],root.get_stu2()[90],root.get_stu2()[132],root.get_stu2()[174],root.get_stu2()[216],root.get_stu2()[258],
                  root.get_stu3()[6],root.get_stu3()[48],root.get_stu3()[90],root.get_stu3()[132],root.get_stu3()[174],root.get_stu3()[216],root.get_stu3()[258],
                  root.get_stu4()[6],root.get_stu4()[48],root.get_stu4()[90],root.get_stu4()[132],root.get_stu4()[174],root.get_stu4()[216],root.get_stu4()[258],
                  root.get_stu5()[6],root.get_stu5()[48],root.get_stu5()[90],root.get_stu5()[132],root.get_stu5()[174],root.get_stu5()[216],root.get_stu5()[258],
                  root.get_stu6()[6],root.get_stu6()[48],root.get_stu6()[90],root.get_stu6()[132],root.get_stu6()[174],root.get_stu6()[216],root.get_stu6()[258],
                  root.get_stu7()[6],root.get_stu7()[48],root.get_stu7()[90],root.get_stu7()[132],root.get_stu7()[174],root.get_stu7()[216],root.get_stu7()[258],
                  root.get_stu8()[6],root.get_stu8()[48],root.get_stu8()[90],root.get_stu8()[132],root.get_stu8()[174],root.get_stu8()[216],root.get_stu8()[258],
                  root.get_stu9()[6],root.get_stu9()[48],root.get_stu9()[90],root.get_stu9()[132],root.get_stu9()[174],root.get_stu9()[216],root.get_stu9()[258],
                  root.get_stu10()[6],root.get_stu10()[48],root.get_stu10()[90],root.get_stu10()[132],root.get_stu10()[174],root.get_stu10()[216],root.get_stu10()[258]]
            GI1 = 0
            for item in gi:
                        if 0 < item < 50:
                              GI1 = GI1+1
            root.num[96].delete(0, tk.END)
            root.num[96].insert(0, GI1)
            x25 = (GI1 * float(root.per1.get())) / 100
            root.num[99].delete(0, tk.END)
            root.num[99].insert(0, x25)
            
            GI2 = 0
            for item in gi:
                        if  item >= 50:
                              GI2 = GI2+1
            root.num[100].delete(0, tk.END)
            root.num[100].insert(0, GI2)
            x26 = (GI2 * float(root.per1.get())) / 100
            root.num[103].delete(0, tk.END)
            root.num[103].insert(0, x26)
            
            GI3 = 0
            for item in gi:
                        if  item >= 75:
                              GI3 = GI3+1
            root.num[104].delete(0, tk.END)
            root.num[104].insert(0, GI3)
            x27 = (GI3 * float(root.per1.get())) / 100
            root.num[107].delete(0, tk.END)
            root.num[107].insert(0, x27)
            
            GI4 = 0
            for item in gi:
                        if  item >= 85:
                              GI4 = GI4+1
            root.num[108].delete(0, tk.END)
            root.num[108].insert(0, GI4)
            x28 = (GI4 * float(root.per1.get())) / 100
            root.num[111].delete(0, tk.END)
            root.num[111].insert(0, x28)
            
            G1 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and 0 < gi[q] <= 49:
                      G1.append(q)
                  q=q+1
           
            root.num[97].delete(0, tk.END)
            root.num[97].insert(0, len(G1))
            root.num[98].delete(0, tk.END)
            root.num[98].insert(0, GI1 - len(G1))
            
            G2 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  gi[q] >= 50:
                      G2.append(q)
                  q=q+1
           
            root.num[101].delete(0, tk.END)
            root.num[101].insert(0, len(G2))
            root.num[102].delete(0, tk.END)
            root.num[102].insert(0, GI2 - len(G2))
            
            G3 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  gi[q] >= 75:
                      G3.append(q)
                  q=q+1
           
            root.num[105].delete(0, tk.END)
            root.num[105].insert(0, len(G3))
            root.num[106].delete(0, tk.END)
            root.num[106].insert(0, GI3 - len(G3))
            
            G4 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  gi[q] >= 85:
                      G4.append(q)
                  q=q+1
           
            root.num[109].delete(0, tk.END)
            root.num[109].insert(0, len(G4))
            root.num[110].delete(0, tk.END)
            root.num[110].insert(0, GI4 - len(G4))
            
            #HISTORY
            
            hi = [root.get_stu1()[7],root.get_stu1()[49],root.get_stu1()[91],root.get_stu1()[133],root.get_stu1()[175],root.get_stu1()[217],root.get_stu1()[259],
                  root.get_stu2()[7],root.get_stu2()[49],root.get_stu2()[91],root.get_stu2()[133],root.get_stu2()[175],root.get_stu2()[217],root.get_stu2()[259],
                  root.get_stu3()[7],root.get_stu3()[49],root.get_stu3()[91],root.get_stu3()[133],root.get_stu3()[175],root.get_stu3()[217],root.get_stu3()[259],
                  root.get_stu4()[7],root.get_stu4()[49],root.get_stu4()[91],root.get_stu4()[133],root.get_stu4()[175],root.get_stu4()[217],root.get_stu4()[259],
                  root.get_stu5()[7],root.get_stu5()[49],root.get_stu5()[91],root.get_stu5()[133],root.get_stu5()[175],root.get_stu5()[217],root.get_stu5()[259],
                  root.get_stu6()[7],root.get_stu6()[49],root.get_stu6()[91],root.get_stu6()[133],root.get_stu6()[175],root.get_stu6()[217],root.get_stu6()[259],
                  root.get_stu7()[7],root.get_stu7()[49],root.get_stu7()[91],root.get_stu7()[133],root.get_stu7()[175],root.get_stu7()[217],root.get_stu7()[259],
                  root.get_stu8()[7],root.get_stu8()[49],root.get_stu8()[91],root.get_stu8()[133],root.get_stu8()[175],root.get_stu8()[217],root.get_stu8()[259],
                  root.get_stu9()[7],root.get_stu9()[49],root.get_stu9()[91],root.get_stu9()[133],root.get_stu9()[175],root.get_stu9()[217],root.get_stu9()[259],
                  root.get_stu10()[7],root.get_stu10()[49],root.get_stu10()[91],root.get_stu10()[133],root.get_stu10()[175],root.get_stu10()[217],root.get_stu10()[259]]
            
            HI1 = 0
            for item in hi:
                        if 0 < item < 50:
                              HI1 = HI1+1
            root.num[112].delete(0, tk.END)
            root.num[112].insert(0, HI1)
            x30 = (HI1 * float(root.per1.get())) / 100
            root.num[115].delete(0, tk.END)
            root.num[115].insert(0, x30)
            
            
            
            HI2 = 0
            for item in hi:
                        if  item >= 50:
                              HI2 = HI2+1
            root.num[116].delete(0, tk.END)
            root.num[116].insert(0, HI2)
            x31 = (HI2 * float(root.per1.get())) / 100
            root.num[119].delete(0, tk.END)
            root.num[119].insert(0, x31)
            
            HI3 = 0
            for item in hi:
                        if  item >= 75:
                              HI3 = HI3+1
            root.num[120].delete(0, tk.END)
            root.num[120].insert(0, HI3)
            x32 = (HI3 * float(root.per1.get())) / 100
            root.num[123].delete(0, tk.END)
            root.num[123].insert(0, x32)
            
            HI4 = 0
            for item in hi:
                        if  item >= 85:
                              HI4 = HI4+1
            root.num[124].delete(0, tk.END)
            root.num[124].insert(0, HI4)
            x33 = (HI4 * float(root.per1.get())) / 100
            root.num[127].delete(0, tk.END)
            root.num[127].insert(0, x33)
            
            H1 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and 0 < hi[q] <= 49:
                      H1.append(q)
                  q=q+1
           
            root.num[113].delete(0, tk.END)
            root.num[113].insert(0, len(H1))
            root.num[114].delete(0, tk.END)
            root.num[114].insert(0, HI1 - len(H1))
            
            H2 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  hi[q] >= 50:
                      H2.append(q)
                  q=q+1
           
            root.num[117].delete(0, tk.END)
            root.num[117].insert(0, len(H2))
            root.num[118].delete(0, tk.END)
            root.num[118].insert(0, HI2 - len(H2))
            
            H3 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  hi[q] >= 75:
                      H3.append(q)
                  q=q+1
           
            root.num[121].delete(0, tk.END)
            root.num[121].insert(0, len(H3))
            root.num[122].delete(0, tk.END)
            root.num[122].insert(0, HI3 - len(H3))
            
            H4 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  hi[q] >= 85:
                      H4.append(q)
                  q=q+1
           
            root.num[125].delete(0, tk.END)
            root.num[125].insert(0, len(H4))
            root.num[126].delete(0, tk.END)
            root.num[126].insert(0, HI4 - len(H4))
            
           #CIVICS
            
            ci = [root.get_stu1()[8],root.get_stu1()[50],root.get_stu1()[92],root.get_stu1()[134],root.get_stu1()[176],root.get_stu1()[218],root.get_stu1()[260],
                  root.get_stu2()[8],root.get_stu2()[50],root.get_stu2()[92],root.get_stu2()[134],root.get_stu2()[176],root.get_stu2()[218],root.get_stu2()[260],
                  root.get_stu3()[8],root.get_stu3()[50],root.get_stu3()[92],root.get_stu3()[134],root.get_stu3()[176],root.get_stu3()[218],root.get_stu3()[260],
                  root.get_stu4()[8],root.get_stu4()[50],root.get_stu4()[92],root.get_stu4()[134],root.get_stu4()[176],root.get_stu4()[218],root.get_stu4()[260],
                  root.get_stu5()[8],root.get_stu5()[50],root.get_stu5()[92],root.get_stu5()[134],root.get_stu5()[176],root.get_stu5()[218],root.get_stu5()[260],
                  root.get_stu6()[8],root.get_stu6()[50],root.get_stu6()[92],root.get_stu6()[134],root.get_stu6()[176],root.get_stu6()[218],root.get_stu6()[260],
                  root.get_stu7()[8],root.get_stu7()[50],root.get_stu7()[92],root.get_stu7()[134],root.get_stu7()[176],root.get_stu7()[218],root.get_stu7()[260],
                  root.get_stu8()[8],root.get_stu8()[50],root.get_stu8()[92],root.get_stu8()[134],root.get_stu8()[176],root.get_stu8()[218],root.get_stu8()[260],
                  root.get_stu9()[8],root.get_stu9()[50],root.get_stu9()[92],root.get_stu9()[134],root.get_stu9()[176],root.get_stu9()[218],root.get_stu9()[260],
                  root.get_stu10()[8],root.get_stu10()[50],root.get_stu10()[92],root.get_stu10()[134],root.get_stu10()[176],root.get_stu10()[218],root.get_stu10()[260]] 
            CI1 = 0
            for item in ci:
                        if 0 < item < 50:
                              CI1 = CI1+1
            root.num[128].delete(0, tk.END)
            root.num[128].insert(0, CI1)
            x34 = (CI1 * float(root.per1.get())) / 100
            root.num[131].delete(0, tk.END)
            root.num[131].insert(0, x34)
            
            CI2 = 0
            for item in ci:
                        if item >= 50:
                              CI2 = CI2+1
            root.num[132].delete(0, tk.END)
            root.num[132].insert(0, CI2)
            x35 = (CI2 * float(root.per1.get())) / 100
            root.num[135].delete(0, tk.END)
            root.num[135].insert(0, x35)
            
            CI3 = 0
            for item in ci:
                        if item >= 75:
                              CI3 = CI3+1
            root.num[136].delete(0, tk.END)
            root.num[136].insert(0, CI3)
            x36 = (CI3 * float(root.per1.get())) / 100
            root.num[139].delete(0, tk.END)
            root.num[139].insert(0, x36)
            
            CI4 = 0
            for item in ci:
                        if item >= 85:
                              CI4 = CI4+1
            root.num[140].delete(0, tk.END)
            root.num[140].insert(0, CI4)
            x37 = (CI4 * float(root.per1.get())) / 100
            root.num[143].delete(0, tk.END)
            root.num[143].insert(0, x37)
            
            C1 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and 0 < ci[q] <= 49:
                      C1.append(q)
                  q=q+1
           
            root.num[129].delete(0, tk.END)
            root.num[129].insert(0, len(C1))
            root.num[130].delete(0, tk.END)
            root.num[130].insert(0, CI1 - len(C1))
            
            C2 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and ci[q] >= 50:
                      C2.append(q)
                  q=q+1
           
            root.num[133].delete(0, tk.END)
            root.num[133].insert(0, len(C2))
            root.num[134].delete(0, tk.END)
            root.num[134].insert(0, CI2 - len(C2))
            
            C3 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and ci[q] >= 75:
                      C3.append(q)
                  q=q+1
           
            root.num[137].delete(0, tk.END)
            root.num[137].insert(0, len(C3))
            root.num[138].delete(0, tk.END)
            root.num[138].insert(0, CI3 - len(C3))
            
            C4 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and ci[q] >= 85:
                      C4.append(q)
                  q=q+1
           
            root.num[141].delete(0, tk.END)
            root.num[141].insert(0, len(C4))
            root.num[142].delete(0, tk.END)
            root.num[142].insert(0, CI4 - len(C4))
            
            #HPE
            
            HPE =[root.get_stu1()[9],root.get_stu1()[51],root.get_stu1()[93],root.get_stu1()[135],root.get_stu1()[177],root.get_stu1()[219],root.get_stu1()[261],
                  root.get_stu2()[9],root.get_stu2()[51],root.get_stu2()[93],root.get_stu2()[135],root.get_stu2()[177],root.get_stu2()[219],root.get_stu2()[261],
                  root.get_stu3()[9],root.get_stu3()[51],root.get_stu3()[93],root.get_stu3()[135],root.get_stu3()[177],root.get_stu3()[219],root.get_stu3()[261],
                  root.get_stu4()[9],root.get_stu4()[51],root.get_stu4()[93],root.get_stu4()[135],root.get_stu4()[177],root.get_stu4()[219],root.get_stu4()[261],
                  root.get_stu5()[9],root.get_stu5()[51],root.get_stu5()[93],root.get_stu5()[135],root.get_stu5()[177],root.get_stu5()[219],root.get_stu5()[261],
                  root.get_stu6()[9],root.get_stu6()[51],root.get_stu6()[93],root.get_stu6()[135],root.get_stu6()[177],root.get_stu6()[219],root.get_stu6()[261],
                  root.get_stu7()[9],root.get_stu7()[51],root.get_stu7()[93],root.get_stu7()[135],root.get_stu7()[177],root.get_stu7()[219],root.get_stu7()[261],
                  root.get_stu8()[9],root.get_stu8()[51],root.get_stu8()[93],root.get_stu8()[135],root.get_stu8()[177],root.get_stu8()[219],root.get_stu8()[261],
                  root.get_stu9()[9],root.get_stu9()[51],root.get_stu9()[93],root.get_stu9()[135],root.get_stu9()[177],root.get_stu9()[219],root.get_stu9()[261],
                  root.get_stu10()[9],root.get_stu10()[51],root.get_stu10()[93],root.get_stu10()[135],root.get_stu10()[177],root.get_stu10()[219],root.get_stu10()[261]]
            HP1 = 0
            for item in HPE:
                        if 0 < item < 50:
                              HP1 = HP1+1
            root.num[144].delete(0, tk.END)
            root.num[144].insert(0, HP1)
            x38 = (HP1 * float(root.per1.get())) / 100
            root.num[147].delete(0, tk.END)
            root.num[147].insert(0, x38)
            
            HP2 = 0
            for item in HPE:
                        if  item >= 50:
                              HP2 = HP2+1
            root.num[148].delete(0, tk.END)
            root.num[148].insert(0, HP2)
            x39 = (HP2 * float(root.per1.get())) / 100
            root.num[151].delete(0, tk.END)
            root.num[151].insert(0, x39)
            
            HP3 = 0
            for item in HPE:
                        if  item >= 75:
                              HP3 = HP3+1
            root.num[152].delete(0, tk.END)
            root.num[152].insert(0, HP3)
            x40 = (HP3 * float(root.per1.get())) / 100
            root.num[155].delete(0, tk.END)
            root.num[155].insert(0, x40)
            
            HP4 = 0
            for item in HPE:
                        if  item >= 85:
                              HP4 = HP4 + 1
            root.num[156].delete(0, tk.END)
            root.num[156].insert(0, HP4)
            x41 = (HP4 * float(root.per1.get())) / 100
            root.num[159].delete(0, tk.END)
            root.num[159].insert(0, x41)
            
            HPE1 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and 0 < HPE[q] <= 49:
                      HPE1.append(q)
                  q=q+1
           
            root.num[145].delete(0, tk.END)
            root.num[145].insert(0, len(HPE1))
            root.num[146].delete(0, tk.END)
            root.num[146].insert(0, HP1 - len(HPE1))
            
            HPE2 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  HPE[q] >= 50:
                      HPE2.append(q)
                  q=q+1
           
            root.num[149].delete(0, tk.END)
            root.num[149].insert(0, len(HPE2))
            root.num[150].delete(0, tk.END)
            root.num[150].insert(0, HP2 - len(HPE2))
            
            HPE3 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and   HPE[q] >= 75:
                      HPE3.append(q)
                  q=q+1
           
            root.num[153].delete(0, tk.END)
            root.num[153].insert(0, len(HPE3))
            root.num[154].delete(0, tk.END)
            root.num[154].insert(0, HP3 - len(HPE3))
            
            HPE4 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and   HPE[q] >= 85:
                      HPE4.append(q)
                  q=q+1
           
            root.num[157].delete(0, tk.END)
            root.num[157].insert(0, len(HPE4))
            root.num[158].delete(0, tk.END)
            root.num[158].insert(0, HP4 - len(HPE4))
            
            #IT
            
            IT  = [root.get_stu1()[10],root.get_stu1()[52],root.get_stu1()[94],root.get_stu1()[136],root.get_stu1()[178],root.get_stu1()[220],root.get_stu1()[262],
                  root.get_stu2()[10],root.get_stu2()[52],root.get_stu2()[94],root.get_stu2()[136],root.get_stu2()[178],root.get_stu2()[220],root.get_stu2()[262],
                  root.get_stu3()[10],root.get_stu3()[52],root.get_stu3()[94],root.get_stu3()[136],root.get_stu3()[178],root.get_stu3()[220],root.get_stu3()[262],
                  root.get_stu4()[10],root.get_stu4()[52],root.get_stu4()[94],root.get_stu4()[136],root.get_stu4()[178],root.get_stu4()[220],root.get_stu4()[262],
                  root.get_stu5()[10],root.get_stu5()[52],root.get_stu5()[94],root.get_stu5()[136],root.get_stu5()[178],root.get_stu5()[220],root.get_stu5()[262],
                  root.get_stu6()[10],root.get_stu6()[52],root.get_stu6()[94],root.get_stu6()[136],root.get_stu6()[178],root.get_stu6()[220],root.get_stu6()[262],
                  root.get_stu7()[10],root.get_stu7()[52],root.get_stu7()[94],root.get_stu7()[136],root.get_stu7()[178],root.get_stu7()[220],root.get_stu7()[262],
                  root.get_stu8()[10],root.get_stu8()[52],root.get_stu8()[94],root.get_stu8()[136],root.get_stu8()[178],root.get_stu8()[220],root.get_stu8()[262],
                  root.get_stu9()[10],root.get_stu9()[52],root.get_stu9()[94],root.get_stu9()[136],root.get_stu9()[178],root.get_stu9()[220],root.get_stu9()[262],
                  root.get_stu10()[10],root.get_stu10()[52],root.get_stu10()[94],root.get_stu10()[136],root.get_stu10()[178],root.get_stu10()[220],root.get_stu10()[262]] 
            
            IT1 = 0
            for item in IT:
                        if 0 < item < 50:
                              IT1 = IT1+1
            root.num[160].delete(0, tk.END)
            root.num[160].insert(0, IT1)
            x42 = (IT1 * float(root.per1.get())) / 100
            root.num[163].delete(0, tk.END)
            root.num[163].insert(0, x42)
            
            IT2 = 0
            for item in IT:
                        if  item >= 50:
                              IT2 = IT2+1
            root.num[164].delete(0, tk.END)
            root.num[164].insert(0, IT2)
            x43 = (IT2 * float(root.per1.get())) / 100
            root.num[167].delete(0, tk.END)
            root.num[167].insert(0, x43)
            
            IT3 = 0
            for item in IT:
                        if  item >= 75:
                              IT3 = IT3+1
            root.num[168].delete(0, tk.END)
            root.num[168].insert(0, IT3)
            x44 = (IT3 * float(root.per1.get())) / 100
            root.num[171].delete(0, tk.END)
            root.num[171].insert(0, x44)
            
            IT4 = 0
            for item in IT:
                        if  item >= 85:
                              IT4 = IT4+1
            root.num[172].delete(0, tk.END)
            root.num[172].insert(0, IT4)
            x45 = (IT4 * float(root.per1.get())) / 100
            root.num[175].delete(0, tk.END)
            root.num[175].insert(0, x45)
            
            T1 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and 0 < IT[q] <= 49:
                      T1.append(q)
                  q=q+1
           
            root.num[161].delete(0, tk.END)
            root.num[161].insert(0, len(T1))
            root.num[162].delete(0, tk.END)
            root.num[162].insert(0, IT1 - len(T1))
            
            T2 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and IT[q] >= 50:
                      T2.append(q)
                  q=q+1
           
            root.num[165].delete(0, tk.END)
            root.num[165].insert(0, len(T2))
            root.num[166].delete(0, tk.END)
            root.num[166].insert(0, IT2 - len(T2))
            
            T3 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and IT[q] >= 75:
                      T3.append(q)
                  q=q+1
           
            root.num[169].delete(0, tk.END)
            root.num[169].insert(0, len(T3))
            root.num[170].delete(0, tk.END)
            root.num[170].insert(0, IT3 - len(T3))
            
            T4 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and IT[q] >= 85:
                      T4.append(q)
                  q=q+1
           
            root.num[173].delete(0, tk.END)
            root.num[173].insert(0, len(T4))
            root.num[174].delete(0, tk.END)
            root.num[174].insert(0, IT4 - len(T4))
            
            
            
        def Add3(root):
        
            AM = [root.get_stu1()[28],root.get_stu1()[70],root.get_stu1()[112],root.get_stu1()[154],root.get_stu1()[196],root.get_stu1()[238],root.get_stu1()[280],
                  root.get_stu2()[28],root.get_stu2()[70],root.get_stu2()[112],root.get_stu2()[154],root.get_stu2()[196],root.get_stu2()[238],root.get_stu2()[280],
                  root.get_stu3()[28],root.get_stu3()[70],root.get_stu3()[112],root.get_stu3()[154],root.get_stu3()[196],root.get_stu3()[238],root.get_stu3()[280],
                  root.get_stu4()[28],root.get_stu4()[70],root.get_stu4()[112],root.get_stu4()[154],root.get_stu4()[196],root.get_stu4()[238],root.get_stu4()[280],
                  root.get_stu5()[28],root.get_stu5()[70],root.get_stu5()[112],root.get_stu5()[154],root.get_stu5()[196],root.get_stu5()[238],root.get_stu5()[280],
                  root.get_stu6()[28],root.get_stu6()[70],root.get_stu6()[112],root.get_stu6()[154],root.get_stu6()[196],root.get_stu6()[238],root.get_stu6()[280],
                  root.get_stu7()[28],root.get_stu7()[70],root.get_stu7()[112],root.get_stu7()[154],root.get_stu7()[196],root.get_stu7()[238],root.get_stu7()[280],
                  root.get_stu8()[28],root.get_stu8()[70],root.get_stu8()[112],root.get_stu8()[154],root.get_stu8()[196],root.get_stu8()[238],root.get_stu8()[280],
                  root.get_stu9()[28],root.get_stu9()[70],root.get_stu9()[112],root.get_stu9()[154],root.get_stu9()[196],root.get_stu9()[238],root.get_stu9()[280],
                  root.get_stu10()[28],root.get_stu10()[70],root.get_stu10()[112],root.get_stu10()[154],root.get_stu10()[196],root.get_stu10()[238],root.get_stu10()[280]]
           
            sex = [root.sex1.get(),root.sex2.get(),root.sex3.get(),root.sex4.get(),                    
                  root.sex5.get(),root.sex6.get(),root.sex7.get(),root.sex8.get(),
                  root.sex9.get(),root.sex10.get(),root.sex11.get(),root.sex12.get(),
                  root.sex13.get(),root.sex14.get(),root.sex15.get(),root.sex16.get(),
                  root.sex17.get(),root.sex18.get(),root.sex19.get(),root.sex20.get(),
                  root.sex21.get(),root.sex22.get(),root.sex23.get(),root.sex24.get(),
                  root.sex25.get(),root.sex26.get(),root.sex27.get(),root.sex28.get(),
                  root.sex29.get(),root.sex30.get(),root.sex31.get(),root.sex32.get(),
                  root.sex33.get(),root.sex34.get(),root.sex35.get(),root.sex36.get(),
                  root.sex37.get(),root.sex38.get(),root.sex39.get(),root.sex40.get(),
                  root.sex41.get(),root.sex42.get(),root.sex43.get(),root.sex44.get(),
                  root.sex45.get(),root.sex46.get(),root.sex47.get(),root.sex48.get(),
                  root.sex49.get(),root.sex50.get(),root.sex51.get(),root.sex52.get(),
                  root.sex53.get(),root.sex54.get(),root.sex55.get(),root.sex56.get(),
                  root.sex57.get(),root.sex58.get(),root.sex59.get(),root.sex60.get(),
                  root.sex61.get(),root.sex62.get(),root.sex63.get(),root.sex64.get(),
                  root.sex65.get(),root.sex66.get(),root.sex67.get(),root.sex68.get(),
                  root.sex69.get(),root.sex70.get()]
                                #Amharic
            
            count1 = 0
            for item in AM:
                        if 0 < item < 50:
                              count1 = count1+1
            root.num1[0].delete(0, tk.END)
            root.num1[0].insert(0, count1)         
            x1 = (count1 * float(root.per3.get())) / 100
            root.num1[3].delete(0, tk.END)
            root.num1[3].insert(0, x1) 
            
            count2 = 0
            for item in AM:
                     if item >= 50:
                         count2 = count2+1
            root.num1[4].delete(0, tk.END)
            root.num1[4].insert(0, count2)
            x2 = (count2 * float(root.per3.get())) / 100
            root.num1[7].delete(0, tk.END)
            root.num1[7].insert(0, x2) 
            
            count3 = 0
            for item in AM:
                     if item >= 75:
                         count3 = count3+1
            root.num1[8].delete(0, tk.END)
            root.num1[8].insert(0, count3)
            x3 = (count3 * float(root.per3.get())) / 100
            root.num1[11].delete(0, tk.END)
            root.num1[11].insert(0, x3) 
            
            count4 = 0
            for item in AM:
                     if item >= 85:
                         count4 = count4+1
            root.num1[12].delete(0, tk.END)
            root.num1[12].insert(0, count4)
            x4 = (count4 * float(root.per3.get())) / 100
            root.num1[15].delete(0, tk.END)
            root.num1[15].insert(0, x4)
            
            
            
            AM1 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and 0 < AM[q] <= 49:
                      AM1.append(q)
                  q=q+1
           
            root.num1[1].delete(0, tk.END)
            root.num1[1].insert(0, len(AM1))
            root.num1[2].delete(0, tk.END)
            root.num1[2].insert(0, count1 - len(AM1))

                 
            AM2 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and AM[q] >= 50:
                      AM2.append(q)
                  q=q+1
           
            root.num1[5].delete(0, tk.END)
            root.num1[5].insert(0, len(AM2))
            root.num1[6].delete(0, tk.END)
            root.num1[6].insert(0, count2 - len(AM2))     
                
            
            AM3 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and AM[q] >= 75:
                      AM3.append(q)
                  q=q+1
           
            root.num1[9].delete(0, tk.END)
            root.num1[9].insert(0, len(AM3))
            root.num1[10].delete(0, tk.END)
            root.num1[10].insert(0, count3 - len(AM3)) 
            
            AM4 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and AM[q] >= 85:
                      AM4.append(q)
                  q=q+1
           
            root.num1[13].delete(0, tk.END)
            root.num1[13].insert(0, len(AM4))
            root.num1[14].delete(0, tk.END)
            root.num1[14].insert(0, count4 - len(AM4)) 
            
            
            #ENGLISH
            
            EN = [root.get_stu1()[29],root.get_stu1()[71],root.get_stu1()[113],root.get_stu1()[155],root.get_stu1()[197],root.get_stu1()[239],root.get_stu1()[281],
                  root.get_stu2()[29],root.get_stu2()[71],root.get_stu2()[113],root.get_stu2()[155],root.get_stu2()[197],root.get_stu2()[239],root.get_stu2()[281],
                  root.get_stu3()[29],root.get_stu3()[71],root.get_stu3()[113],root.get_stu3()[155],root.get_stu3()[197],root.get_stu3()[239],root.get_stu3()[281],
                  root.get_stu4()[29],root.get_stu4()[71],root.get_stu4()[113],root.get_stu4()[155],root.get_stu4()[197],root.get_stu4()[239],root.get_stu4()[281],
                  root.get_stu5()[29],root.get_stu5()[71],root.get_stu5()[113],root.get_stu5()[155],root.get_stu5()[197],root.get_stu5()[239],root.get_stu5()[281],
                  root.get_stu6()[29],root.get_stu6()[71],root.get_stu6()[113],root.get_stu6()[155],root.get_stu6()[197],root.get_stu6()[239],root.get_stu6()[281],
                  root.get_stu7()[29],root.get_stu7()[71],root.get_stu7()[113],root.get_stu7()[155],root.get_stu7()[197],root.get_stu7()[239],root.get_stu7()[281],
                  root.get_stu8()[29],root.get_stu8()[71],root.get_stu8()[113],root.get_stu8()[155],root.get_stu8()[197],root.get_stu8()[239],root.get_stu8()[281],
                  root.get_stu9()[29],root.get_stu9()[71],root.get_stu9()[113],root.get_stu9()[155],root.get_stu9()[197],root.get_stu9()[239],root.get_stu9()[281],
                  root.get_stu10()[29],root.get_stu10()[71],root.get_stu10()[113],root.get_stu10()[155],root.get_stu10()[197],root.get_stu10()[239],root.get_stu10()[281]]
            EN1 = 0
            for item in EN:
                        if 0 < item < 50:
                              EN1 = EN1+1
            root.num1[16].delete(0, tk.END)
            root.num1[16].insert(0, EN1) 
            x5 = (EN1 * float(root.per3.get())) / 100
            root.num1[19].delete(0, tk.END)
            root.num1[19].insert(0, x5)
            
            
            
            EN2 = 0
            for item in EN:
                     if item >= 50:
                         EN2 = EN2+1
            root.num1[20].delete(0, tk.END)
            root.num1[20].insert(0, EN2)
            x6 = (EN2 * float(root.per3.get())) / 100
            root.num1[23].delete(0, tk.END)
            root.num1[23].insert(0, x6)
            
            EN3 = 0
            for item in EN:
                     if item >= 75:
                         EN3 = EN3+1
            root.num1[24].delete(0, tk.END)
            root.num1[24].insert(0,EN3)
            x7 = (EN3 * float(root.per3.get())) / 100
            root.num1[27].delete(0, tk.END)
            root.num1[27].insert(0, x7)
            
            EN4 = 0
            for item in EN:
                     if item >= 85:
                         EN4 = EN4+1
            root.num1[28].delete(0, tk.END)
            root.num1[28].insert(0, EN4)
            x8 = (EN3 * float(root.per3.get())) / 100
            root.num1[31].delete(0, tk.END)
            root.num1[31].insert(0, x8)
            
            E1 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and 0 < EN[q] <= 49:
                      E1.append(q)
                  q=q+1
           
            root.num1[17].delete(0, tk.END)
            root.num1[17].insert(0, len(E1))
            root.num1[18].delete(0, tk.END)
            root.num1[18].insert(0, EN1 - len(E1))
            
            E2 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and EN[q] >= 50:
                      E2.append(q)
                  q=q+1
           
            root.num1[21].delete(0, tk.END)
            root.num1[21].insert(0, len(E2))
            root.num1[22].delete(0, tk.END)
            root.num1[22].insert(0, EN2 - len(E2))  
            
            E3 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and EN[q] >= 75:
                      E3.append(q)
                  q=q+1
           
            root.num1[25].delete(0, tk.END)
            root.num1[25].insert(0, len(E3))
            root.num1[26].delete(0, tk.END)
            root.num1[26].insert(0, EN3 - len(E3))
            
            
            E4 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and EN[q] >= 85:
                      E4.append(q)
                  q=q+1
           
            root.num1[29].delete(0, tk.END)
            root.num1[29].insert(0, len(E4))
            root.num1[30].delete(0, tk.END)
            root.num1[30].insert(0, EN4 - len(E4))
            
            #MATHES
            
            MA = [root.get_stu1()[30],root.get_stu1()[72],root.get_stu1()[114],root.get_stu1()[156],root.get_stu1()[198],root.get_stu1()[240],root.get_stu1()[282],
                  root.get_stu2()[30],root.get_stu2()[72],root.get_stu2()[114],root.get_stu2()[156],root.get_stu2()[198],root.get_stu2()[240],root.get_stu2()[282],
                  root.get_stu3()[30],root.get_stu3()[72],root.get_stu3()[114],root.get_stu3()[156],root.get_stu3()[198],root.get_stu3()[240],root.get_stu3()[282],
                  root.get_stu4()[30],root.get_stu4()[72],root.get_stu4()[114],root.get_stu4()[156],root.get_stu4()[198],root.get_stu4()[240],root.get_stu4()[282],
                  root.get_stu5()[30],root.get_stu5()[72],root.get_stu5()[114],root.get_stu5()[156],root.get_stu5()[198],root.get_stu5()[240],root.get_stu5()[282],
                  root.get_stu6()[30],root.get_stu6()[72],root.get_stu6()[114],root.get_stu6()[156],root.get_stu6()[198],root.get_stu6()[240],root.get_stu6()[282],
                  root.get_stu7()[30],root.get_stu7()[72],root.get_stu7()[114],root.get_stu7()[156],root.get_stu7()[198],root.get_stu7()[240],root.get_stu7()[282],
                  root.get_stu8()[30],root.get_stu8()[72],root.get_stu8()[114],root.get_stu8()[156],root.get_stu8()[198],root.get_stu8()[240],root.get_stu8()[282],
                  root.get_stu9()[30],root.get_stu9()[72],root.get_stu9()[114],root.get_stu9()[156],root.get_stu9()[198],root.get_stu9()[240],root.get_stu9()[282],
                  root.get_stu10()[30],root.get_stu10()[72],root.get_stu10()[114],root.get_stu10()[156],root.get_stu10()[198],root.get_stu10()[240],root.get_stu10()[282]] 
            
            MA1 = 0
            for item in MA:
                        if 0 < item < 50:
                              MA1 = MA1+1
            root.num1[32].delete(0, tk.END)
            root.num1[32].insert(0, MA1) 
            x9 = (MA1 * float(root.per3.get())) / 100
            root.num1[35].delete(0, tk.END)
            root.num1[35].insert(0, x9)
            
            MA2 = 0
            for item in MA:
                     if item >= 50:
                         MA2 = MA2+1
            root.num1[36].delete(0, tk.END)
            root.num1[36].insert(0, MA2)
            x10 = (MA2 * float(root.per3.get())) / 100
            root.num1[39].delete(0, tk.END)
            root.num1[39].insert(0, x10)
            
            MA3 = 0
            for item in MA:
                     if item >= 75:
                         MA3 = MA3+1
            root.num1[40].delete(0, tk.END)
            root.num1[40].insert(0,MA3)
            x11 = (MA3 * float(root.per3.get())) / 100
            root.num1[43].delete(0, tk.END)
            root.num1[43].insert(0, x11)
            
            MA4 = 0
            for item in MA:
                     if item >= 85:
                         MA4 = MA4+1
            root.num1[44].delete(0, tk.END)
            root.num1[44].insert(0, MA4)
            x12 = (MA4 * float(root.per3.get())) / 100
            root.num1[47].delete(0, tk.END)
            root.num1[47].insert(0, x12)
            
            M1 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and 0 < MA[q] <= 49:
                      M1.append(q)
                  q=q+1
           
            root.num1[33].delete(0, tk.END)
            root.num1[33].insert(0, len(M1))
            root.num1[34].delete(0, tk.END)
            root.num1[34].insert(0, MA1 - len(M1))
            
            M2 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and MA[q] >= 50:
                      M2.append(q)
                  q=q+1
           
            root.num1[37].delete(0, tk.END)
            root.num1[37].insert(0, len(M2))
            root.num1[38].delete(0, tk.END)
            root.num1[38].insert(0, MA2 - len(M2))  
            
            M3 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and MA[q] >= 75:
                      M3.append(q)
                  q=q+1
           
            root.num1[41].delete(0, tk.END)
            root.num1[41].insert(0, len(M3))
            root.num1[42].delete(0, tk.END)
            root.num1[42].insert(0, MA3 - len(M3))
            
            M4 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and MA[q] >= 85:
                      M4.append(q)
                  q=q+1
           
            root.num1[45].delete(0, tk.END)
            root.num1[45].insert(0, len(M4))
            root.num1[46].delete(0, tk.END)
            root.num1[46].insert(0, MA4 - len(M4))
            
            #PYHISICS
            
            ph = [root.get_stu1()[31],root.get_stu1()[73],root.get_stu1()[115],root.get_stu1()[157],root.get_stu1()[199],root.get_stu1()[241],root.get_stu1()[283],
                  root.get_stu2()[31],root.get_stu2()[73],root.get_stu2()[115],root.get_stu2()[157],root.get_stu2()[199],root.get_stu2()[241],root.get_stu2()[283],
                  root.get_stu3()[31],root.get_stu3()[73],root.get_stu3()[115],root.get_stu3()[157],root.get_stu3()[199],root.get_stu3()[241],root.get_stu3()[283],
                  root.get_stu4()[31],root.get_stu4()[73],root.get_stu4()[115],root.get_stu4()[157],root.get_stu4()[199],root.get_stu4()[241],root.get_stu4()[283],
                  root.get_stu5()[31],root.get_stu5()[73],root.get_stu5()[115],root.get_stu5()[157],root.get_stu5()[199],root.get_stu5()[241],root.get_stu5()[283],
                  root.get_stu6()[31],root.get_stu6()[73],root.get_stu6()[115],root.get_stu6()[157],root.get_stu6()[199],root.get_stu6()[241],root.get_stu6()[283],
                  root.get_stu7()[31],root.get_stu7()[73],root.get_stu7()[115],root.get_stu7()[157],root.get_stu7()[199],root.get_stu7()[241],root.get_stu7()[283],
                  root.get_stu8()[31],root.get_stu8()[73],root.get_stu8()[115],root.get_stu8()[157],root.get_stu8()[199],root.get_stu8()[241],root.get_stu8()[283],
                  root.get_stu9()[31],root.get_stu9()[73],root.get_stu9()[115],root.get_stu9()[157],root.get_stu9()[199],root.get_stu9()[241],root.get_stu9()[283],
                  root.get_stu10()[31],root.get_stu10()[73],root.get_stu10()[115],root.get_stu10()[157],root.get_stu10()[199],root.get_stu10()[241],root.get_stu10()[283]]
            PH1 = 0
            for item in ph:
                        if 0 < item < 50:
                              PH1 = PH1+1
            root.num1[48].delete(0, tk.END)
            root.num1[48].insert(0, PH1)
            x13 = (PH1 * float(root.per3.get())) / 100
            root.num1[51].delete(0, tk.END)
            root.num1[51].insert(0, x13)            
            
            PH2 = 0
            for item in ph:
                     if item >= 50:
                         PH2 = PH2+1
            root.num1[52].delete(0, tk.END)
            root.num1[52].insert(0, PH2)
            x14 = (PH2 * float(root.per3.get())) / 100
            root.num1[55].delete(0, tk.END)
            root.num1[55].insert(0, x14)
            
            PH3 = 0
            for item in ph:
                     if item >= 75:
                         PH3 = PH3+1
            root.num1[56].delete(0, tk.END)
            root.num1[56].insert(0, PH3)
            x15 = (PH3 * float(root.per3.get())) / 100
            root.num1[59].delete(0, tk.END)
            root.num1[59].insert(0, x15)
            
            
            PH4 = 0
            for item in ph:
                     if item >= 85:
                         PH4 = PH4+1
            root.num1[60].delete(0, tk.END)
            root.num1[60].insert(0, PH4)
            x16 = (PH4 * float(root.per3.get())) / 100
            root.num1[63].delete(0, tk.END)
            root.num1[63].insert(0, x16)
            
            p1 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and 0 < ph[q] <= 49:
                      p1.append(q)
                  q=q+1
           
            root.num1[49].delete(0, tk.END)
            root.num1[49].insert(0, len(p1))
            root.num1[50].delete(0, tk.END)
            root.num1[50].insert(0, PH1 - len(p1))
            
            p2 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and ph[q] >= 50:
                      p2.append(q)
                  q=q+1
           
            root.num1[53].delete(0, tk.END)
            root.num1[53].insert(0, len(p2))
            root.num1[54].delete(0, tk.END)
            root.num1[54].insert(0, PH2 - len(p2))
            
            p3 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and ph[q] >= 75:
                      p3.append(q)
                  q=q+1
           
            root.num1[57].delete(0, tk.END)
            root.num1[57].insert(0, len(p3))
            root.num1[58].delete(0, tk.END)
            root.num1[58].insert(0, PH3 - len(p3))
            
            p4 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and ph[q] >= 85:
                      p4.append(q)
                  q=q+1
           
            root.num1[61].delete(0, tk.END)
            root.num1[61].insert(0, len(p4))
            root.num1[62].delete(0, tk.END)
            root.num1[62].insert(0, PH4 - len(p4))
            

            #CHEMISTRY
            
            ch = [root.get_stu1()[32],root.get_stu1()[74],root.get_stu1()[116],root.get_stu1()[158],root.get_stu1()[200],root.get_stu1()[242],root.get_stu1()[284],
                  root.get_stu2()[32],root.get_stu2()[74],root.get_stu2()[116],root.get_stu2()[158],root.get_stu2()[200],root.get_stu2()[242],root.get_stu2()[284],
                  root.get_stu3()[32],root.get_stu3()[74],root.get_stu3()[116],root.get_stu3()[158],root.get_stu3()[200],root.get_stu3()[242],root.get_stu3()[284],
                  root.get_stu4()[32],root.get_stu4()[74],root.get_stu4()[116],root.get_stu4()[158],root.get_stu4()[200],root.get_stu4()[242],root.get_stu4()[284],
                  root.get_stu5()[32],root.get_stu5()[74],root.get_stu5()[116],root.get_stu5()[158],root.get_stu5()[200],root.get_stu5()[242],root.get_stu5()[284],
                  root.get_stu6()[32],root.get_stu6()[74],root.get_stu6()[116],root.get_stu6()[158],root.get_stu6()[200],root.get_stu6()[242],root.get_stu6()[284],
                  root.get_stu7()[32],root.get_stu7()[74],root.get_stu7()[116],root.get_stu7()[158],root.get_stu7()[200],root.get_stu7()[242],root.get_stu7()[284],
                  root.get_stu8()[32],root.get_stu8()[74],root.get_stu8()[116],root.get_stu8()[158],root.get_stu8()[200],root.get_stu8()[242],root.get_stu8()[284],
                  root.get_stu9()[32],root.get_stu9()[74],root.get_stu9()[116],root.get_stu9()[158],root.get_stu9()[200],root.get_stu9()[242],root.get_stu9()[284],
                  root.get_stu10()[32],root.get_stu10()[74],root.get_stu10()[116],root.get_stu10()[158],root.get_stu10()[200],root.get_stu10()[242],root.get_stu10()[284]]             
            CH1 = 0
            for item in ch:
                        if 0 < item < 50:
                              CH1 = CH1+1
            root.num1[64].delete(0, tk.END)
            root.num1[64].insert(0, CH1)
            x17 = (CH1 * float(root.per3.get())) / 100
            root.num1[67].delete(0, tk.END)
            root.num1[67].insert(0, x17)
            
            CH2 = 0
            for item in ch:
                        if item >= 50:
                              CH2 = CH2+1
            root.num1[68].delete(0, tk.END)
            root.num1[68].insert(0, CH2)
            x18 = (CH2 * float(root.per3.get())) / 100
            root.num1[71].delete(0, tk.END)
            root.num1[71].insert(0, x18)
            
            CH3 = 0
            for item in ch:
                        if item >= 75:
                              CH3 = CH3+1
            root.num1[72].delete(0, tk.END)
            root.num1[72].insert(0, CH3)
            x19 = (CH3 * float(root.per3.get())) / 100
            root.num1[75].delete(0, tk.END)
            root.num1[75].insert(0, x19)
            
            CH4 = 0
            for item in ch:
                        if item >= 85:
                              CH4 = CH4+1
            root.num1[76].delete(0, tk.END)
            root.num1[76].insert(0, CH4)
            x20 = (CH4 * float(root.per3.get())) / 100
            root.num1[79].delete(0, tk.END)
            root.num1[79].insert(0, x20)
            
            C1 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and 0 < ch[q] <= 49:
                      C1.append(q)
                  q=q+1
           
            root.num1[65].delete(0, tk.END)
            root.num1[65].insert(0, len(C1))
            root.num1[66].delete(0, tk.END)
            root.num1[66].insert(0, CH1 - len(C1))
            
            C2 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  ch[q] >= 50:
                      C2.append(q)
                  q=q+1
           
            root.num1[69].delete(0, tk.END)
            root.num1[69].insert(0, len(C2))
            root.num1[70].delete(0, tk.END)
            root.num1[70].insert(0, CH2 - len(C2))
            
            
            C3 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  ch[q] >= 75:
                      C3.append(q)
                  q=q+1
           
            root.num1[73].delete(0, tk.END)
            root.num1[73].insert(0, len(C3))
            root.num1[74].delete(0, tk.END)
            root.num1[74].insert(0, CH3 - len(C3))
            
            C4 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  ch[q] >= 85:
                      C4.append(q)
                  q=q+1
           
            root.num1[77].delete(0, tk.END)
            root.num1[77].insert(0, len(C4))
            root.num1[78].delete(0, tk.END)
            root.num1[78].insert(0, CH4 - len(C4))
            
            
            #BIOLOGY
            
            bi = [root.get_stu1()[33],root.get_stu1()[75],root.get_stu1()[117],root.get_stu1()[159],root.get_stu1()[201],root.get_stu1()[243],root.get_stu1()[285],
                  root.get_stu2()[33],root.get_stu2()[75],root.get_stu2()[117],root.get_stu2()[159],root.get_stu2()[201],root.get_stu2()[243],root.get_stu2()[285],
                  root.get_stu3()[33],root.get_stu3()[75],root.get_stu3()[117],root.get_stu3()[159],root.get_stu3()[201],root.get_stu3()[243],root.get_stu3()[285],
                  root.get_stu4()[33],root.get_stu4()[75],root.get_stu4()[117],root.get_stu4()[159],root.get_stu4()[201],root.get_stu4()[243],root.get_stu4()[285],
                  root.get_stu5()[33],root.get_stu5()[75],root.get_stu5()[117],root.get_stu5()[159],root.get_stu5()[201],root.get_stu5()[243],root.get_stu5()[285],
                  root.get_stu6()[33],root.get_stu6()[75],root.get_stu6()[117],root.get_stu6()[159],root.get_stu6()[201],root.get_stu6()[243],root.get_stu6()[285],
                  root.get_stu7()[33],root.get_stu7()[75],root.get_stu7()[117],root.get_stu7()[159],root.get_stu7()[201],root.get_stu7()[243],root.get_stu7()[285],
                  root.get_stu8()[33],root.get_stu8()[75],root.get_stu8()[117],root.get_stu8()[159],root.get_stu8()[201],root.get_stu8()[243],root.get_stu8()[285],
                  root.get_stu9()[33],root.get_stu9()[75],root.get_stu9()[117],root.get_stu9()[159],root.get_stu9()[201],root.get_stu9()[243],root.get_stu9()[285],
                  root.get_stu10()[33],root.get_stu10()[75],root.get_stu10()[117],root.get_stu10()[159],root.get_stu10()[201],root.get_stu10()[243],root.get_stu10()[285]]
            BI1 = 0
            for item in bi:
                        if 0 < item < 50:
                              BI1 = BI1+1
            root.num1[80].delete(0, tk.END)
            root.num1[80].insert(0, BI1)
            x21 = (BI1 * float(root.per3.get())) / 100
            root.num1[83].delete(0, tk.END)
            root.num1[83].insert(0, x21)
            
            BI2 = 0
            for item in bi:
                        if item >= 50:
                              BI2 = BI2+1
            root.num1[84].delete(0, tk.END)
            root.num1[84].insert(0, BI2)
            x22 = (BI2 * float(root.per3.get())) / 100
            root.num1[87].delete(0, tk.END)
            root.num1[87].insert(0, x22)
            
            BI3 = 0
            for item in bi:
                        if item >= 75:
                              BI3 = BI3+1
            root.num1[88].delete(0, tk.END)
            root.num1[88].insert(0, BI3)
            x23 = (BI3 * float(root.per3.get())) / 100
            root.num1[91].delete(0, tk.END)
            root.num1[91].insert(0, x23)
            
            BI4 = 0
            for item in bi:
                        if item >= 85:
                              BI4 = BI4+1
            root.num1[92].delete(0, tk.END)
            root.num1[92].insert(0, BI4)
            x24 = (BI4 * float(root.per3.get())) / 100
            root.num1[95].delete(0, tk.END)
            root.num1[95].insert(0, x24)
            
            B1 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and 0 < bi[q] <= 49:
                      B1.append(q)
                  q=q+1
           
            root.num1[81].delete(0, tk.END)
            root.num1[81].insert(0, len(B1))
            root.num1[82].delete(0, tk.END)
            root.num1[82].insert(0, BI1 - len(B1))
            
            
            B2 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  bi[q] >= 50:
                      B2.append(q)
                  q=q+1
           
            root.num1[85].delete(0, tk.END)
            root.num1[85].insert(0, len(B2))
            root.num1[86].delete(0, tk.END)
            root.num1[86].insert(0, BI2 - len(B2))
            
            B3 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  bi[q] >= 75:
                      B3.append(q)
                  q=q+1
           
            root.num1[89].delete(0, tk.END)
            root.num1[89].insert(0, len(B3))
            root.num1[90].delete(0, tk.END)
            root.num1[90].insert(0, BI3 - len(B3))
            
            B4 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  bi[q] >= 85:
                      B4.append(q)
                  q=q+1
           
            root.num1[93].delete(0, tk.END)
            root.num1[93].insert(0, len(B4))
            root.num1[94].delete(0, tk.END)
            root.num1[94].insert(0, BI4 - len(B4))
            
            #GEOGRAPHY
            
            gi = [root.get_stu1()[34],root.get_stu1()[76],root.get_stu1()[118],root.get_stu1()[160],root.get_stu1()[202],root.get_stu1()[244],root.get_stu1()[286],
                  root.get_stu2()[34],root.get_stu2()[76],root.get_stu2()[118],root.get_stu2()[160],root.get_stu2()[202],root.get_stu2()[244],root.get_stu2()[286],
                  root.get_stu3()[34],root.get_stu3()[76],root.get_stu3()[118],root.get_stu3()[160],root.get_stu3()[202],root.get_stu3()[244],root.get_stu3()[286],
                  root.get_stu4()[34],root.get_stu4()[76],root.get_stu4()[118],root.get_stu4()[160],root.get_stu4()[202],root.get_stu4()[244],root.get_stu4()[286],
                  root.get_stu5()[34],root.get_stu5()[76],root.get_stu5()[118],root.get_stu5()[160],root.get_stu5()[202],root.get_stu5()[244],root.get_stu5()[286],
                  root.get_stu6()[34],root.get_stu6()[76],root.get_stu6()[118],root.get_stu6()[160],root.get_stu6()[202],root.get_stu6()[244],root.get_stu6()[286],
                  root.get_stu7()[34],root.get_stu7()[76],root.get_stu7()[118],root.get_stu7()[160],root.get_stu7()[202],root.get_stu7()[244],root.get_stu7()[286],
                  root.get_stu8()[34],root.get_stu8()[76],root.get_stu8()[118],root.get_stu8()[160],root.get_stu8()[202],root.get_stu8()[244],root.get_stu8()[286],
                  root.get_stu9()[34],root.get_stu9()[76],root.get_stu9()[118],root.get_stu9()[160],root.get_stu9()[202],root.get_stu9()[244],root.get_stu9()[286],
                  root.get_stu10()[34],root.get_stu10()[76],root.get_stu10()[118],root.get_stu10()[160],root.get_stu10()[202],root.get_stu10()[244],root.get_stu10()[286]]
            GI1 = 0
            for item in gi:
                        if 0 < item < 50:
                              GI1 = GI1+1
            root.num1[96].delete(0, tk.END)
            root.num1[96].insert(0, GI1)
            x25 = (GI1 * float(root.per3.get())) / 100
            root.num1[99].delete(0, tk.END)
            root.num1[99].insert(0, x25)
            
            GI2 = 0
            for item in gi:
                        if  item >= 50:
                              GI2 = GI2+1
            root.num1[100].delete(0, tk.END)
            root.num1[100].insert(0, GI2)
            x26 = (GI2 * float(root.per3.get())) / 100
            root.num1[103].delete(0, tk.END)
            root.num1[103].insert(0, x26)
            
            GI3 = 0
            for item in gi:
                        if  item >= 75:
                              GI3 = GI3+1
            root.num1[104].delete(0, tk.END)
            root.num1[104].insert(0, GI3)
            x27 = (GI3 * float(root.per3.get())) / 100
            root.num1[107].delete(0, tk.END)
            root.num1[107].insert(0, x27)
            
            GI4 = 0
            for item in gi:
                        if  item >= 85:
                              GI4 = GI4+1
            root.num1[108].delete(0, tk.END)
            root.num1[108].insert(0, GI4)
            x28 = (GI4 * float(root.per3.get())) / 100
            root.num1[111].delete(0, tk.END)
            root.num1[111].insert(0, x28)
            
            G1 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and 0 < gi[q] <= 49:
                      G1.append(q)
                  q=q+1
           
            root.num1[97].delete(0, tk.END)
            root.num1[97].insert(0, len(G1))
            root.num1[98].delete(0, tk.END)
            root.num1[98].insert(0, GI1 - len(G1))
            
            G2 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  gi[q] >= 50:
                      G2.append(q)
                  q=q+1
           
            root.num1[101].delete(0, tk.END)
            root.num1[101].insert(0, len(G2))
            root.num1[102].delete(0, tk.END)
            root.num1[102].insert(0, GI2 - len(G2))
            
            G3 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  gi[q] >= 75:
                      G3.append(q)
                  q=q+1
           
            root.num1[105].delete(0, tk.END)
            root.num1[105].insert(0, len(G3))
            root.num1[106].delete(0, tk.END)
            root.num1[106].insert(0, GI3 - len(G3))
            
            G4 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  gi[q] >= 85:
                      G4.append(q)
                  q=q+1
           
            root.num1[109].delete(0, tk.END)
            root.num1[109].insert(0, len(G4))
            root.num1[110].delete(0, tk.END)
            root.num1[110].insert(0, GI4 - len(G4))
            
            #HISTORY
            
            hi = [root.get_stu1()[35],root.get_stu1()[77],root.get_stu1()[119],root.get_stu1()[161],root.get_stu1()[203],root.get_stu1()[245],root.get_stu1()[287],
                  root.get_stu2()[35],root.get_stu2()[77],root.get_stu2()[119],root.get_stu2()[161],root.get_stu2()[203],root.get_stu2()[245],root.get_stu2()[287],
                  root.get_stu3()[35],root.get_stu3()[77],root.get_stu3()[119],root.get_stu3()[161],root.get_stu3()[203],root.get_stu3()[245],root.get_stu3()[287],
                  root.get_stu4()[35],root.get_stu4()[77],root.get_stu4()[119],root.get_stu4()[161],root.get_stu4()[203],root.get_stu4()[245],root.get_stu4()[287],
                  root.get_stu5()[35],root.get_stu5()[77],root.get_stu5()[119],root.get_stu5()[161],root.get_stu5()[203],root.get_stu5()[245],root.get_stu5()[287],
                  root.get_stu6()[35],root.get_stu6()[77],root.get_stu6()[119],root.get_stu6()[161],root.get_stu6()[203],root.get_stu6()[245],root.get_stu6()[287],
                  root.get_stu7()[35],root.get_stu7()[77],root.get_stu7()[119],root.get_stu7()[161],root.get_stu7()[203],root.get_stu7()[245],root.get_stu7()[287],
                  root.get_stu8()[35],root.get_stu8()[77],root.get_stu8()[119],root.get_stu8()[161],root.get_stu8()[203],root.get_stu8()[245],root.get_stu8()[287],
                  root.get_stu9()[35],root.get_stu9()[77],root.get_stu9()[119],root.get_stu9()[161],root.get_stu9()[203],root.get_stu9()[245],root.get_stu9()[287],
                  root.get_stu10()[35],root.get_stu10()[77],root.get_stu10()[119],root.get_stu10()[161],root.get_stu10()[203],root.get_stu10()[245],root.get_stu10()[287]]
            
            HI1 = 0
            for item in hi:
                        if 0 < item < 50:
                              HI1 = HI1+1
            root.num1[112].delete(0, tk.END)
            root.num1[112].insert(0, HI1)
            x30 = (HI1 * float(root.per3.get())) / 100
            root.num1[115].delete(0, tk.END)
            root.num1[115].insert(0, x30)
            
            
            
            HI2 = 0
            for item in hi:
                        if  item >= 50:
                              HI2 = HI2+1
            root.num1[116].delete(0, tk.END)
            root.num1[116].insert(0, HI2)
            x31 = (HI2 * float(root.per3.get())) / 100
            root.num1[119].delete(0, tk.END)
            root.num1[119].insert(0, x31)
            
            HI3 = 0
            for item in hi:
                        if  item >= 75:
                              HI3 = HI3+1
            root.num1[120].delete(0, tk.END)
            root.num1[120].insert(0, HI3)
            x32 = (HI3 * float(root.per3.get())) / 100
            root.num1[123].delete(0, tk.END)
            root.num1[123].insert(0, x32)
            
            HI4 = 0
            for item in hi:
                        if  item >= 85:
                              HI4 = HI4+1
            root.num1[124].delete(0, tk.END)
            root.num1[124].insert(0, HI4)
            x33 = (HI4 * float(root.per3.get())) / 100
            root.num1[127].delete(0, tk.END)
            root.num1[127].insert(0, x33)
            
            H1 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and 0 < hi[q] <= 49:
                      H1.append(q)
                  q=q+1
           
            root.num1[113].delete(0, tk.END)
            root.num1[113].insert(0, len(H1))
            root.num1[114].delete(0, tk.END)
            root.num1[114].insert(0, HI1 - len(H1))
            
            H2 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  hi[q] >= 50:
                      H2.append(q)
                  q=q+1
           
            root.num1[117].delete(0, tk.END)
            root.num1[117].insert(0, len(H2))
            root.num1[118].delete(0, tk.END)
            root.num1[118].insert(0, HI2 - len(H2))
            
            H3 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  hi[q] >= 75:
                      H3.append(q)
                  q=q+1
           
            root.num1[121].delete(0, tk.END)
            root.num1[121].insert(0, len(H3))
            root.num1[122].delete(0, tk.END)
            root.num1[122].insert(0, HI3 - len(H3))
            
            H4 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  hi[q] >= 85:
                      H4.append(q)
                  q=q+1
           
            root.num1[125].delete(0, tk.END)
            root.num1[125].insert(0, len(H4))
            root.num1[126].delete(0, tk.END)
            root.num1[126].insert(0, HI4 - len(H4))
            
           #CIVICS
            
            ci = [root.get_stu1()[36],root.get_stu1()[78],root.get_stu1()[120],root.get_stu1()[162],root.get_stu1()[204],root.get_stu1()[246],root.get_stu1()[288],
                  root.get_stu2()[36],root.get_stu2()[78],root.get_stu2()[120],root.get_stu2()[162],root.get_stu2()[204],root.get_stu2()[246],root.get_stu2()[288],
                  root.get_stu3()[36],root.get_stu3()[78],root.get_stu3()[120],root.get_stu3()[162],root.get_stu3()[204],root.get_stu3()[246],root.get_stu3()[288],
                  root.get_stu4()[36],root.get_stu4()[78],root.get_stu4()[120],root.get_stu4()[162],root.get_stu4()[204],root.get_stu4()[246],root.get_stu4()[288],
                  root.get_stu5()[36],root.get_stu5()[78],root.get_stu5()[120],root.get_stu5()[162],root.get_stu5()[204],root.get_stu5()[246],root.get_stu5()[288],
                  root.get_stu6()[36],root.get_stu6()[78],root.get_stu6()[120],root.get_stu6()[162],root.get_stu6()[204],root.get_stu6()[246],root.get_stu6()[288],
                  root.get_stu7()[36],root.get_stu7()[78],root.get_stu7()[120],root.get_stu7()[162],root.get_stu7()[204],root.get_stu7()[246],root.get_stu7()[288],
                  root.get_stu8()[36],root.get_stu8()[78],root.get_stu8()[120],root.get_stu8()[162],root.get_stu8()[204],root.get_stu8()[246],root.get_stu8()[288],
                  root.get_stu9()[36],root.get_stu9()[78],root.get_stu9()[120],root.get_stu9()[162],root.get_stu9()[204],root.get_stu9()[246],root.get_stu9()[288],
                  root.get_stu10()[36],root.get_stu10()[78],root.get_stu10()[120],root.get_stu10()[162],root.get_stu10()[204],root.get_stu10()[246],root.get_stu10()[288]]
            CI1 = 0
            for item in ci:
                        if 0 < item < 50:
                              CI1 = CI1+1
            root.num1[128].delete(0, tk.END)
            root.num1[128].insert(0, CI1)
            x34 = (CI1 * float(root.per3.get())) / 100
            root.num1[131].delete(0, tk.END)
            root.num1[131].insert(0, x34)
            
            CI2 = 0
            for item in ci:
                        if item >= 50:
                              CI2 = CI2+1
            root.num1[132].delete(0, tk.END)
            root.num1[132].insert(0, CI2)
            x35 = (CI2 * float(root.per3.get())) / 100
            root.num1[135].delete(0, tk.END)
            root.num1[135].insert(0, x35)
            
            CI3 = 0
            for item in ci:
                        if item >= 75:
                              CI3 = CI3+1
            root.num1[136].delete(0, tk.END)
            root.num1[136].insert(0, CI3)
            x36 = (CI3 * float(root.per3.get())) / 100
            root.num1[139].delete(0, tk.END)
            root.num1[139].insert(0, x36)
            
            CI4 = 0
            for item in ci:
                        if item >= 85:
                              CI4 = CI4+1
            root.num1[140].delete(0, tk.END)
            root.num1[140].insert(0, CI4)
            x37 = (CI4 * float(root.per3.get())) / 100
            root.num1[143].delete(0, tk.END)
            root.num1[143].insert(0, x37)
            
            C1 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and 0 < ci[q] <= 49:
                      C1.append(q)
                  q=q+1
           
            root.num1[129].delete(0, tk.END)
            root.num1[129].insert(0, len(C1))
            root.num1[130].delete(0, tk.END)
            root.num1[130].insert(0, CI1 - len(C1))
            
            C2 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and ci[q] >= 50:
                      C2.append(q)
                  q=q+1
           
            root.num1[133].delete(0, tk.END)
            root.num1[133].insert(0, len(C2))
            root.num1[134].delete(0, tk.END)
            root.num1[134].insert(0, CI2 - len(C2))
            
            C3 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and ci[q] >= 75:
                      C3.append(q)
                  q=q+1
           
            root.num1[137].delete(0, tk.END)
            root.num1[137].insert(0, len(C3))
            root.num1[138].delete(0, tk.END)
            root.num1[138].insert(0, CI3 - len(C3))
            
            C4 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and ci[q] >= 85:
                      C4.append(q)
                  q=q+1
           
            root.num1[141].delete(0, tk.END)
            root.num1[141].insert(0, len(C4))
            root.num1[142].delete(0, tk.END)
            root.num1[142].insert(0, CI4 - len(C4))
            
            #HPE
            
            HPE =[root.get_stu1()[37],root.get_stu1()[79],root.get_stu1()[121],root.get_stu1()[163],root.get_stu1()[205],root.get_stu1()[247],root.get_stu1()[289],
                  root.get_stu2()[37],root.get_stu2()[79],root.get_stu2()[121],root.get_stu2()[163],root.get_stu2()[205],root.get_stu2()[247],root.get_stu2()[289],
                  root.get_stu3()[37],root.get_stu3()[79],root.get_stu3()[121],root.get_stu3()[163],root.get_stu3()[205],root.get_stu3()[247],root.get_stu3()[289],
                  root.get_stu4()[37],root.get_stu4()[79],root.get_stu4()[121],root.get_stu4()[163],root.get_stu4()[205],root.get_stu4()[247],root.get_stu4()[289],
                  root.get_stu5()[37],root.get_stu5()[79],root.get_stu5()[121],root.get_stu5()[163],root.get_stu5()[205],root.get_stu5()[247],root.get_stu5()[289],
                  root.get_stu6()[37],root.get_stu6()[79],root.get_stu6()[121],root.get_stu6()[163],root.get_stu6()[205],root.get_stu6()[247],root.get_stu6()[289],
                  root.get_stu7()[37],root.get_stu7()[79],root.get_stu7()[121],root.get_stu7()[163],root.get_stu7()[205],root.get_stu7()[247],root.get_stu7()[289],
                  root.get_stu8()[37],root.get_stu8()[79],root.get_stu8()[121],root.get_stu8()[163],root.get_stu8()[205],root.get_stu8()[247],root.get_stu8()[289],
                  root.get_stu9()[37],root.get_stu9()[79],root.get_stu9()[121],root.get_stu9()[163],root.get_stu9()[205],root.get_stu9()[247],root.get_stu9()[289],
                  root.get_stu10()[37],root.get_stu10()[79],root.get_stu10()[121],root.get_stu10()[163],root.get_stu10()[205],root.get_stu10()[247],root.get_stu10()[289]]
            HP1 = 0
            for item in HPE:
                        if 0 < item < 50:
                              HP1 = HP1+1
            root.num1[144].delete(0, tk.END)
            root.num1[144].insert(0, HP1)
            x38 = (HP1 * float(root.per3.get())) / 100
            root.num1[147].delete(0, tk.END)
            root.num1[147].insert(0, x38)
            
            HP2 = 0
            for item in HPE:
                        if  item >= 50:
                              HP2 = HP2+1
            root.num1[148].delete(0, tk.END)
            root.num1[148].insert(0, HP2)
            x39 = (HP2 * float(root.per3.get())) / 100
            root.num1[151].delete(0, tk.END)
            root.num1[151].insert(0, x39)
            
            HP3 = 0
            for item in HPE:
                        if  item >= 75:
                              HP3 = HP3+1
            root.num1[152].delete(0, tk.END)
            root.num1[152].insert(0, HP3)
            x40 = (HP3 * float(root.per3.get())) / 100
            root.num1[155].delete(0, tk.END)
            root.num1[155].insert(0, x40)
            
            HP4 = 0
            for item in HPE:
                        if  item >= 85:
                              HP4 = HP4 + 1
            root.num1[156].delete(0, tk.END)
            root.num1[156].insert(0, HP4)
            x41 = (HP4 * float(root.per3.get())) / 100
            root.num1[159].delete(0, tk.END)
            root.num1[159].insert(0, x41)
            
            HPE1 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and 0 < HPE[q] <= 49:
                      HPE1.append(q)
                  q=q+1
           
            root.num1[145].delete(0, tk.END)
            root.num1[145].insert(0, len(HPE1))
            root.num1[146].delete(0, tk.END)
            root.num1[146].insert(0, HP1 - len(HPE1))
            
            HPE2 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and  HPE[q] >= 50:
                      HPE2.append(q)
                  q=q+1
           
            root.num1[149].delete(0, tk.END)
            root.num1[149].insert(0, len(HPE2))
            root.num1[150].delete(0, tk.END)
            root.num1[150].insert(0, HP2 - len(HPE2))
            
            HPE3 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and   HPE[q] >= 75:
                      HPE3.append(q)
                  q=q+1
           
            root.num1[153].delete(0, tk.END)
            root.num1[153].insert(0, len(HPE3))
            root.num1[154].delete(0, tk.END)
            root.num1[154].insert(0, HP3 - len(HPE3))
            
            HPE4 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and   HPE[q] >= 85:
                      HPE4.append(q)
                  q=q+1
           
            root.num1[157].delete(0, tk.END)
            root.num1[157].insert(0, len(HPE4))
            root.num1[158].delete(0, tk.END)
            root.num1[158].insert(0, HP4 - len(HPE4))
            
            #IT
            
            IT  =[root.get_stu1()[38],root.get_stu1()[80],root.get_stu1()[122],root.get_stu1()[164],root.get_stu1()[206],root.get_stu1()[248],root.get_stu1()[290],
                  root.get_stu2()[38],root.get_stu2()[80],root.get_stu2()[122],root.get_stu2()[164],root.get_stu2()[206],root.get_stu2()[248],root.get_stu2()[290],
                  root.get_stu3()[38],root.get_stu3()[80],root.get_stu3()[122],root.get_stu3()[164],root.get_stu3()[206],root.get_stu3()[248],root.get_stu3()[290],
                  root.get_stu4()[38],root.get_stu4()[80],root.get_stu4()[122],root.get_stu4()[164],root.get_stu4()[206],root.get_stu4()[248],root.get_stu4()[290],
                  root.get_stu5()[38],root.get_stu5()[80],root.get_stu5()[122],root.get_stu5()[164],root.get_stu5()[206],root.get_stu5()[248],root.get_stu5()[290],
                  root.get_stu6()[38],root.get_stu6()[80],root.get_stu6()[122],root.get_stu6()[164],root.get_stu6()[206],root.get_stu6()[248],root.get_stu6()[290],
                  root.get_stu7()[38],root.get_stu7()[80],root.get_stu7()[122],root.get_stu7()[164],root.get_stu7()[206],root.get_stu7()[248],root.get_stu7()[290],
                  root.get_stu8()[38],root.get_stu8()[80],root.get_stu8()[122],root.get_stu8()[164],root.get_stu8()[206],root.get_stu8()[248],root.get_stu8()[290],
                  root.get_stu9()[38],root.get_stu9()[80],root.get_stu9()[122],root.get_stu9()[164],root.get_stu9()[206],root.get_stu9()[248],root.get_stu9()[290],
                  root.get_stu10()[38],root.get_stu10()[80],root.get_stu10()[122],root.get_stu10()[164],root.get_stu10()[206],root.get_stu10()[248],root.get_stu10()[290]]
            
            IT1 = 0
            for item in IT:
                        if 0 < item < 50:
                              IT1 = IT1+1
            root.num1[160].delete(0, tk.END)
            root.num1[160].insert(0, IT1)
            x42 = (IT1 * float(root.per3.get())) / 100
            root.num1[163].delete(0, tk.END)
            root.num1[163].insert(0, x42)
            
            IT2 = 0
            for item in IT:
                        if  item >= 50:
                              IT2 = IT2+1
            root.num1[164].delete(0, tk.END)
            root.num1[164].insert(0, IT2)
            x43 = (IT2 * float(root.per3.get())) / 100
            root.num1[167].delete(0, tk.END)
            root.num1[167].insert(0, x43)
            
            IT3 = 0
            for item in IT:
                        if  item >= 75:
                              IT3 = IT3+1
            root.num1[168].delete(0, tk.END)
            root.num1[168].insert(0, IT3)
            x44 = (IT3 * float(root.per3.get())) / 100
            root.num1[171].delete(0, tk.END)
            root.num1[171].insert(0, x44)
            
            IT4 = 0
            for item in IT:
                        if  item >= 85:
                              IT4 = IT4+1
            root.num1[172].delete(0, tk.END)
            root.num1[172].insert(0, IT4)
            x45 = (IT4 * float(root.per3.get())) / 100
            root.num1[175].delete(0, tk.END)
            root.num1[175].insert(0, x45)
            
            T1 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and 0 < IT[q] <= 49:
                      T1.append(q)
                  q=q+1
           
            root.num1[161].delete(0, tk.END)
            root.num1[161].insert(0, len(T1))
            root.num1[162].delete(0, tk.END)
            root.num1[162].insert(0, IT1 - len(T1))
            
            T2 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and IT[q] >= 50:
                      T2.append(q)
                  q=q+1
           
            root.num1[165].delete(0, tk.END)
            root.num1[165].insert(0, len(T2))
            root.num1[166].delete(0, tk.END)
            root.num1[166].insert(0, IT2 - len(T2))
            
            T3 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and IT[q] >= 75:
                      T3.append(q)
                  q=q+1
           
            root.num1[169].delete(0, tk.END)
            root.num1[169].insert(0, len(T3))
            root.num1[170].delete(0, tk.END)
            root.num1[170].insert(0, IT3 - len(T3))
            
            T4 = []       
            q = 0
            while q <= 69: 
                  if  sex[q] == "M" and IT[q] >= 85:
                      T4.append(q)
                  q=q+1
           
            root.num1[173].delete(0, tk.END)
            root.num1[173].insert(0, len(T4))
            root.num1[174].delete(0, tk.END)
            root.num1[174].insert(0, IT4 - len(T4))
                

            
            
        def create_widgets(root):

                                   #root 
                root.intro = Label(root, text = "በየነ GENERAL SECONDARY SCHOOL ROSTER", font = ("Arial", 10)) 
                root.intro.grid(column = 0, row = 0, columnspan = 10)
                root.year = Label(root, text = "YEAR...........................................", font = ("Arial", 10)) 
                root. year.grid(column = 0, row = 1,columnspan = 15)
                root. gread = Label(root, text = "GR............................................", font = ("Arial", 10)) 
                root. gread.grid(column = 2, row = 1,columnspan = 15)
                root.section = Label(root, text = "SECTION..................................", font = ("Arial", 10)) 
                root.section.grid(column = 3, row = 1,columnspan = 35)
                root. nam1 = Label(root, text = "1st H.R.T Name.................................................................SIG................................................................", font = ("Arial", 10)) 
                root.nam1.grid(column = 1, row = 27, columnspan = 20)
                root.nam1 = Label(root, text = "2nd H.R.T Name..........................................................SIG............DIRECTOR'S NAME:- EWUNETIE ADDIS.SIG.....................", font = ("Arial", 10)) 
                root. nam1.grid(column = 2, row = 28, columnspan = 20)
              
                root.txt1 = Label(root, text = ".",width=5)
                root.txt1.grid(column=0, row=4)

                root.txt2 = ttk.Entry(root,  width=3,font = ("Arial",8, "bold"))
                root.txt2.grid(column=1, row=4)
                root.txt2.insert(0,'No')
                root.txt3 = ttk.Entry(root,  width=20,font = ("Arial",8,"bold"))
                root.txt3.grid(column=2, row=4)
                root.txt3.insert(0,'NAME')
                root.txt4 = ttk.Entry(root,  width=6,font = ("Arial",8, "bold"))
                root.txt4.grid(column=3, row=4)
                root.txt4.insert(0,'SEX')
                root.txt5 = ttk.Entry(root, width=6,font = ("Arial",8, "bold"))
                root.txt5.grid(column=4, row=4)
                root.txt5.insert(0,'AGE')
                root.txt6 = ttk.Entry(root,  width=8,font = ("Arial",8, "bold"))
                root.txt6.grid(column=5, row=4)
                root.txt6.insert(0,'SEM')
                root.txt7 = ttk.Entry(root,  width=8,font = ("Arial",8, "bold"))
                root.txt7.grid(column=6, row=4)
                root.txt7.insert(0,'AM')
                root.txt8 = ttk.Entry(root,  width=8,font = ("Arial",8, "bold"))
                root.txt8.grid(column=7, row=4)
                root.txt8.insert(0,'EN')
                root.txt9 = ttk.Entry(root,  width=8,font = ("Arial",8, "bold"))
                root.txt9.grid(column=8, row=4)
                root.txt9.insert(0,'MA')
                root.txt10 = ttk.Entry(root,  width=8,font = ("Arial",8, "bold"))
                root.txt10.grid(column=9, row=4)
                root.txt10.insert(0,'PH')
                root.txt11 = ttk.Entry(root,  width=8,font = ("Arial",8, "bold"))
                root.txt11.grid(column=10, row=4)
                root.txt11.insert(0,'CH')
                root.txt12 = ttk.Entry(root,  width=8,font = ("Arial",8, "bold"))
                root.txt12.grid(column=11, row=4)
                root.txt12.insert(0,'BI')
                root.txt13 = ttk.Entry(root,  width=8,font = ("Arial",8, "bold"))
                root.txt13.grid(column=12, row=4)
                root.txt13.insert(0,'GI')
                root.txt14 = ttk.Entry(root,  width=8,font = ("Arial",8, "bold"))
                root.txt14.grid(column=13, row=4)
                root.txt14.insert(0,'HI')
                root.txt15 = ttk.Entry(root,  width=8,font = ("Arial",8, "bold"))
                root.txt15.grid(column=14, row=4)
                root.txt15.insert(0,'CV')
                root.txt16 = ttk.Entry(root,  width=8,font = ("Arial",8, "bold"))
                root.txt16.grid(column=15, row=4)
                root.txt16.insert(0,'HP')
                root.txt16 = ttk.Entry(root,  width=8,font = ("Arial",8, "bold"))
                root.txt16.grid(column=16, row=4)
                root.txt16.insert(0,'IT')
                root.txt17 = ttk.Entry(root,  width=8,font = ("Arial",8, "bold"))
                root.txt17.grid(column=17, row=4)
                root.txt17.insert(0,'SUM')
                root.txt18 = ttk.Entry(root,  width=8,font = ("Arial",8, "bold"))
                root.txt18.grid(column=18, row=4)
                root.txt18.insert(0,'AVRG')
                root.txt19 = ttk.Entry(root,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=19, row=4)
                root.txt19.insert(0,'RANK')
                root.txt19 = ttk.Entry(root,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=20, row=4)
                root.txt19.insert(0,'ATEND')
                root.txt19 = ttk.Entry(root,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=21, row=4)
                root.txt19.insert(0,'COND')
                root.txt19 = ttk.Entry(root,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=22, row=4)
                root.txt19.insert(0,'RMARK')

                                #sex
                root.sex1= ttk.Entry(root,   width=6)
                root.sex1.grid(column=3, row= 5 ,  rowspan = 3,ipady = 33 ) 

                root.sex2= ttk.Entry(root,   width=6)
                root.sex2.grid(column=3, row= 8 ,  rowspan = 3,ipady = 33 ) 
                
                root.sex3= ttk.Entry(root,   width=6)
                root.sex3.grid(column=3, row= 11 ,  rowspan = 3,ipady = 33 )

                root.sex4= ttk.Entry(root,   width=6)
                root.sex4.grid(column=3, row= 14 ,  rowspan = 3,ipady = 33 )

                root.sex5= ttk.Entry(root,   width=6)
                root.sex5.grid(column=3, row= 17 ,  rowspan = 3,ipady = 33 )

                root.sex6= ttk.Entry(root,   width=6)
                root.sex6.grid(column=3, row= 20 ,  rowspan = 3,ipady = 33 )

                root.sex7= ttk.Entry(root,   width=6)
                root.sex7.grid(column=3, row= 23 ,  rowspan = 3,ipady = 33 )                 


                        #number
                i = 0
                s= 1
                while i <= 20 and s<= 8:                
                      root.txt0 = ttk.Entry(root, width=3)
                      root.txt0.grid(column=1, row=5+i  ,rowspan = 3,ipady = 33)
                      root.txt0.insert(0, s)
                                          #name
                      root.txt0 = tk.Text(root, height =1,width=15)
                      root.txt0.grid(column=2, row = 5+i,rowspan = 3,ipady = 33) 
                                            
                       
                                           #Age                  
                      root.txt0 = ttk.Entry(root,   width=6)
                      root.txt0.grid(column=4, row= 5  + i ,  rowspan = 3,ipady = 33 ) 
                                           # ATEND
                      txt0 = ttk.Entry(root,   width=8)
                      txt0.grid(column=19, row= 5+i ,  rowspan = 3,ipady = 33 )

                                           # REMARK
                      txt0 = ttk.Entry(root,   width=8)
                      txt0.grid(column=20, row= 5+ i ,  rowspan = 3,ipady = 33 ) 
                                            # COND
                      txt0 = ttk.Entry(root,   width=8)
                      txt0.grid(column=21, row= 5+i ,  rowspan = 3,ipady = 33 )
                                            # cond
                      txt0 = ttk.Entry(root,   width=8)
                      txt0.grid(column=22, row= 5 + i ,  rowspan = 3,ipady = 33 )
                      
                      i = i + 3 
                      s= s + 1      
                                           #semister
                for xd in range(21): 
                  
                  
                  root.txt0 = ttk.Entry(root, width=8,font = ("Arial",9, "bold"))
                  root.txt0.grid(column=5, row=xd + 5, ipady =4)
                  if xd==0 or xd==3 or xd==6 or xd==9 or xd==12 or xd==15 or xd==18:
                     root.txt0.insert(0, "1st")  
                  if xd==1 or xd==4 or xd==7 or xd==10 or xd==13 or xd==16 or xd==19:
                     root.txt0.insert(0, "2nd")
                  if xd==2 or xd==5 or xd==8 or xd==11 or xd==14 or xd==17 or xd==20:
                     root.txt0.insert(0, "Avrg")
         
                                #crateing the entry box

                root.stu1M = []
                for xd in range(21):
                    for dx in range(14):  
                          root.stu1 = ttk.Entry(root, width=8)
                          root.stu1.grid(column=dx +6, row=xd + 5, ipady =4)         
                          root.stu1M.append(root.stu1)
                          root.stu1.insert(0,'0')
                          
                
                                 #Buttones
                root.btn = ttk.Button(root, text = 'Add', command=root.Add)
                root.btn.grid(column=1, row=27, columnspan = 2)   
                root.btn2 = ttk.Button(root, text ="Inset", command = root.ADD4)
                root.btn2.grid(column = 3, row=27, columnspan = 2)                
                root.btn = ttk.Button(root, text = "next page", command=root.Next_page1)
                root.btn.grid(column=19, row=27, columnspan = 4) 
                #root.btn = ttk.Button(root, text = "Filter page", command=root.filter)
                #root.btn.grid(column=19, row=27, columnspan = 4)                  
                
                
        def Next_page1(root):
                root1 = Tk()
                root1.title('Page -2')
                root.intro = Label(root1, text = "MOTTA GENERAL SECONDARY SCHOOL ROSTER", font = ("Arial", 10)) 
                root.intro.grid(column = 0, row = 0, columnspan = 10)
                root.year = Label(root1, text = "YEAR...........................................", font = ("Arial", 10)) 
                root. year.grid(column = 0, row = 1,columnspan = 15)
                root. gread = Label(root1, text = "GR............................................", font = ("Arial", 10)) 
                root. gread.grid(column = 2, row = 1,columnspan = 15)
                root.section = Label(root1, text = "SECTION..................................", font = ("Arial", 10)) 
                root.section.grid(column = 3, row = 1,columnspan = 35)
                root. nam1 = Label(root1, text = "1st H.R.T Name.................................................................SIG................................................................", font = ("Arial", 10)) 
                root.nam1.grid(column = 1, row = 27, columnspan = 20)
                root.nam1 = Label(root1, text = "2nd H.R.T Name..........................................................SIG............DIRECTOR'S NAME:- EWUNETIE ADDIS.SIG.....................", font = ("Arial", 10)) 
                root. nam1.grid(column = 2, row = 28, columnspan = 20)
              
                root.txt1 = Label(root1, text = ".",width=5)
                root.txt1.grid(column=0, row=4)

                root.txt2 = ttk.Entry(root1,  width=3,font = ("Arial",8, "bold"))
                root.txt2.grid(column=1, row=4)
                root.txt2.insert(0,'No')
                root.txt3 = ttk.Entry(root1,  width=20,font = ("Arial",8,"bold"))
                root.txt3.grid(column=2, row=4)
                root.txt3.insert(0,'NAME')
                root.txt4 = ttk.Entry(root1,  width=6,font = ("Arial",8, "bold"))
                root.txt4.grid(column=3, row=4)
                root.txt4.insert(0,'SEX')
                root.txt5 = ttk.Entry(root1, width=6,font = ("Arial",8, "bold"))
                root.txt5.grid(column=4, row=4)
                root.txt5.insert(0,'AGE')
                root.txt6 = ttk.Entry(root1,  width=8,font = ("Arial",8, "bold"))
                root.txt6.grid(column=5, row=4)
                root.txt6.insert(0,'SEM')
                root.txt7 = ttk.Entry(root1,  width=8,font = ("Arial",8, "bold"))
                root.txt7.grid(column=6, row=4)
                root.txt7.insert(0,'AM')
                root.txt8 = ttk.Entry(root1,  width=8,font = ("Arial",8, "bold"))
                root.txt8.grid(column=7, row=4)
                root.txt8.insert(0,'EN')
                root.txt9 = ttk.Entry(root1,  width=8,font = ("Arial",8, "bold"))
                root.txt9.grid(column=8, row=4)
                root.txt9.insert(0,'MA')
                root.txt10 = ttk.Entry(root1,  width=8,font = ("Arial",8, "bold"))
                root.txt10.grid(column=9, row=4)
                root.txt10.insert(0,'PH')
                root.txt11 = ttk.Entry(root1,  width=8,font = ("Arial",8, "bold"))
                root.txt11.grid(column=10, row=4)
                root.txt11.insert(0,'CH')
                root.txt12 = ttk.Entry(root1,  width=8,font = ("Arial",8, "bold"))
                root.txt12.grid(column=11, row=4)
                root.txt12.insert(0,'BI')
                root.txt13 = ttk.Entry(root1,  width=8,font = ("Arial",8, "bold"))
                root.txt13.grid(column=12, row=4)
                root.txt13.insert(0,'GI')
                root.txt14 = ttk.Entry(root1,  width=8,font = ("Arial",8, "bold"))
                root.txt14.grid(column=13, row=4)
                root.txt14.insert(0,'HI')
                root.txt15 = ttk.Entry(root1,  width=8,font = ("Arial",8, "bold"))
                root.txt15.grid(column=14, row=4)
                root.txt15.insert(0,'CV')
                root.txt16 = ttk.Entry(root1,  width=8,font = ("Arial",8, "bold"))
                root.txt16.grid(column=15, row=4)
                root.txt16.insert(0,'HP')
                root.txt16 = ttk.Entry(root1,  width=8,font = ("Arial",8, "bold"))
                root.txt16.grid(column=16, row=4)
                root.txt16.insert(0,'IT')
                root.txt17 = ttk.Entry(root1,  width=8,font = ("Arial",8, "bold"))
                root.txt17.grid(column=17, row=4)
                root.txt17.insert(0,'SUM')
                root.txt18 = ttk.Entry(root1,  width=8,font = ("Arial",8, "bold"))
                root.txt18.grid(column=18, row=4)
                root.txt18.insert(0,'AVRG')
                root.txt19 = ttk.Entry(root1,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=19, row=4)
                root.txt19.insert(0,'RANK')
                root.txt19 = ttk.Entry(root1,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=20, row=4)
                root.txt19.insert(0,'ATEND')
                root.txt19 = ttk.Entry(root1,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=21, row=4)
                root.txt19.insert(0,'COND')
                root.txt19 = ttk.Entry(root1,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=22, row=4)
                root.txt19.insert(0,'RMARK')

                                #sex
                root.sex8= ttk.Entry(root1,   width=6)
                root.sex8.grid(column=3, row= 5 ,  rowspan = 3,ipady = 33 ) 

                root.sex9= ttk.Entry(root1,   width=6)
                root.sex9.grid(column=3, row= 8 ,  rowspan = 3,ipady = 33 ) 
                
                root.sex10= ttk.Entry(root1,   width=6)
                root.sex10.grid(column=3, row= 11 ,  rowspan = 3,ipady = 33 )

                root.sex11= ttk.Entry(root1,   width=6)
                root.sex11.grid(column=3, row= 14 ,  rowspan = 3,ipady = 33 )

                root.sex12= ttk.Entry(root1,   width=6)
                root.sex12.grid(column=3, row= 17 ,  rowspan = 3,ipady = 33 )

                root.sex13= ttk.Entry(root1,   width=6)
                root.sex13.grid(column=3, row= 20 ,  rowspan = 3,ipady = 33 )

                root.sex14= ttk.Entry(root1,   width=6)
                root.sex14.grid(column=3, row= 23 ,  rowspan = 3,ipady = 33 )
                  




                  #number
                i = 0
                s= 8
                while i <= 20 and s<= 18:                
                      root.txt0 = ttk.Entry(root1, width=3)
                      root.txt0.grid(column=1, row=5+i  ,rowspan = 3,ipady = 33)
                      root.txt0.insert(0, s)
                               #         #name
                      root.txt0 = tk.Text(root1, height =1,width=15)
                      root.txt0.grid(column=2, row = 5+i,rowspan = 3,ipady = 33)  
       
                      
                                         #Age                  
                      root.txt0 = ttk.Entry(root1,   width=6)
                      root.txt0.grid(column=4, row= 5  + i ,  rowspan = 3,ipady = 33 ) 
                                         # ATEND
                      txt0 = ttk.Entry(root1,   width=8)
                      txt0.grid(column=19, row= 5+i ,  rowspan = 3,ipady = 33 )

                                # REMARK
                      txt0 = ttk.Entry(root1,   width=8)
                      txt0.grid(column=20, row= 5+ i ,  rowspan = 3,ipady = 33 ) 
                                # COND
                      txt0 = ttk.Entry(root1,   width=8)
                      txt0.grid(column=21, row= 5+i ,  rowspan = 3,ipady = 33 )
                                # cond
                      txt0 = ttk.Entry(root1,   width=8)
                      txt0.grid(column=22, row= 5 + i ,  rowspan = 3,ipady = 33 )
                      
                      i = i + 3 
                      s= s + 1      
                                #semister
                for xd in range(21):  
                  root.txt0 = ttk.Entry(root1, width=8 ,font = ("Arial",9, "bold"))
                  root.txt0.grid(column=5, row=xd + 5, ipady =4) 
                  if xd==0 or xd==3 or xd==6 or xd==9 or xd==12 or xd==15 or xd==18:
                     root.txt0.insert(0, "1st")  
                  if xd==1 or xd==4 or xd==7 or xd==10 or xd==13 or xd==16 or xd==19:
                     root.txt0.insert(0, "2nd")
                  if xd==2 or xd==5 or xd==8 or xd==11 or xd==14 or xd==17 or xd==20:
                     root.txt0.insert(0, "Avrg")
         
                                #crateing the entry box

                root.stu2M = []
                for xd in range(21):
                    for dx in range(14):  
                          stu1 = ttk.Entry(root1, width=8)
                          stu1.grid(column=dx +6, row=xd + 5, ipady =4)         
                          root.stu2M.append(stu1)
                          stu1.insert(0,'0')
                          
                
                                 #Buttones
                root.btn = ttk.Button(root1, text = 'Add1', command=root.Add)
                root.btn.grid(column=1, row=27, columnspan = 2)                
                root.btn = ttk.Button(root1, text = "next page", command=root.Next_page2)
                root.btn.grid(column=19, row=27, columnspan = 4) 
                root1.mainloop()             
                
         
        def Next_page2(root):
                root2 = Tk()
                root2.title('Page -3')
                root.intro = Label(root2, text = "MOTTA GENERAL SECONDARY SCHOOL ROSTER", font = ("Arial", 10)) 
                root.intro.grid(column = 0, row = 0, columnspan = 10)
                root.year = Label(root2, text = "YEAR...........................................", font = ("Arial", 10)) 
                root. year.grid(column = 0, row = 1,columnspan = 15)
                root. gread = Label(root2, text = "GR............................................", font = ("Arial", 10)) 
                root. gread.grid(column = 2, row = 1,columnspan = 15)
                root.section = Label(root2, text = "SECTION..................................", font = ("Arial", 10)) 
                root.section.grid(column = 3, row = 1,columnspan = 35)
                root. nam1 = Label(root2, text = "1st H.R.T Name.................................................................SIG................................................................", font = ("Arial", 10)) 
                root.nam1.grid(column = 1, row = 27, columnspan = 20)
                root.nam1 = Label(root2, text = "2nd H.R.T Name..........................................................SIG............DIRECTOR'S NAME:- EWUNETIE ADDIS.SIG.....................", font = ("Arial", 10)) 
                root. nam1.grid(column = 2, row = 28, columnspan = 20)
              
                root.txt1 = Label(root2, text = ".",width=5)
                root.txt1.grid(column=0, row=4)

                root.txt2 = ttk.Entry(root2,  width=3,font = ("Arial",8, "bold"))
                root.txt2.grid(column=1, row=4)
                root.txt2.insert(0,'No')
                root.txt3 = ttk.Entry(root2,  width=20,font = ("Arial",8,"bold"))
                root.txt3.grid(column=2, row=4)
                root.txt3.insert(0,'NAME')
                root.txt4 = ttk.Entry(root2,  width=6,font = ("Arial",8, "bold"))
                root.txt4.grid(column=3, row=4)
                root.txt4.insert(0,'SEX')
                root.txt5 = ttk.Entry(root2, width=6,font = ("Arial",8, "bold"))
                root.txt5.grid(column=4, row=4)
                root.txt5.insert(0,'AGE')
                root.txt6 = ttk.Entry(root2,  width=8,font = ("Arial",8, "bold"))
                root.txt6.grid(column=5, row=4)
                root.txt6.insert(0,'SEM')
                root.txt7 = ttk.Entry(root2,  width=8,font = ("Arial",8, "bold"))
                root.txt7.grid(column=6, row=4)
                root.txt7.insert(0,'AM')
                root.txt8 = ttk.Entry(root2,  width=8,font = ("Arial",8, "bold"))
                root.txt8.grid(column=7, row=4)
                root.txt8.insert(0,'EN')
                root.txt9 = ttk.Entry(root2,  width=8,font = ("Arial",8, "bold"))
                root.txt9.grid(column=8, row=4)
                root.txt9.insert(0,'MA')
                root.txt10 = ttk.Entry(root2,  width=8,font = ("Arial",8, "bold"))
                root.txt10.grid(column=9, row=4)
                root.txt10.insert(0,'PH')
                root.txt11 = ttk.Entry(root2,  width=8,font = ("Arial",8, "bold"))
                root.txt11.grid(column=10, row=4)
                root.txt11.insert(0,'CH')
                root.txt12 = ttk.Entry(root2,  width=8,font = ("Arial",8, "bold"))
                root.txt12.grid(column=11, row=4)
                root.txt12.insert(0,'BI')
                root.txt13 = ttk.Entry(root2,  width=8,font = ("Arial",8, "bold"))
                root.txt13.grid(column=12, row=4)
                root.txt13.insert(0,'GI')
                root.txt14 = ttk.Entry(root2,  width=8,font = ("Arial",8, "bold"))
                root.txt14.grid(column=13, row=4)
                root.txt14.insert(0,'HI')
                root.txt15 = ttk.Entry(root2,  width=8,font = ("Arial",8, "bold"))
                root.txt15.grid(column=14, row=4)
                root.txt15.insert(0,'CV')
                root.txt16 = ttk.Entry(root2,  width=8,font = ("Arial",8, "bold"))
                root.txt16.grid(column=15, row=4)
                root.txt16.insert(0,'HP')
                root.txt16 = ttk.Entry(root2,  width=8,font = ("Arial",8, "bold"))
                root.txt16.grid(column=16, row=4)
                root.txt16.insert(0,'IT')
                root.txt17 = ttk.Entry(root2,  width=8,font = ("Arial",8, "bold"))
                root.txt17.grid(column=17, row=4)
                root.txt17.insert(0,'SUM')
                root.txt18 = ttk.Entry(root2,  width=8,font = ("Arial",8, "bold"))
                root.txt18.grid(column=18, row=4)
                root.txt18.insert(0,'AVRG')
                root.txt19 = ttk.Entry(root2,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=19, row=4)
                root.txt19.insert(0,'RANK')
                root.txt19 = ttk.Entry(root2,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=20, row=4)
                root.txt19.insert(0,'ATEND')
                root.txt19 = ttk.Entry(root2,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=21, row=4)
                root.txt19.insert(0,'COND')
                root.txt19 = ttk.Entry(root2,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=22, row=4)
                root.txt19.insert(0,'RMARK')


                                #sex
                root.sex15= ttk.Entry(root2,   width=6)
                root.sex15.grid(column=3, row= 5 ,  rowspan = 3,ipady = 33 ) 

                root.sex16= ttk.Entry(root2,   width=6)
                root.sex16.grid(column=3, row= 8 ,  rowspan = 3,ipady = 33 ) 
                
                root.sex17= ttk.Entry(root2,   width=6)
                root.sex17.grid(column=3, row= 11 ,  rowspan = 3,ipady = 33 )

                root.sex18= ttk.Entry(root2,   width=6)
                root.sex18.grid(column=3, row= 14 ,  rowspan = 3,ipady = 33 )

                root.sex19= ttk.Entry(root2,   width=6)
                root.sex19.grid(column=3, row= 17 ,  rowspan = 3,ipady = 33 )

                root.sex20= ttk.Entry(root2,   width=6)
                root.sex20.grid(column=3, row= 20 ,  rowspan = 3,ipady = 33 )

                root.sex21= ttk.Entry(root2,   width=6)
                root.sex21.grid(column=3, row= 23 ,  rowspan = 3,ipady = 33 )
                  
                
                        #number
                i = 0
                s= 15
                while i <= 20 and s<= 25:                
                      root.txt0 = ttk.Entry(root2, width=3)
                      root.txt0.grid(column=1, row=5+i  ,rowspan = 3,ipady = 33)
                      root.txt0.insert(0, s)
                              #name
                      root.txt0 = tk.Text(root2, height =1,width=15)
                      root.txt0.grid(column=2, row = 5+i,rowspan = 3,ipady = 33)  
                         
                              #Age                  
                      root.txt0 = ttk.Entry(root2,   width=6)
                      root.txt0.grid(column=4, row= 5  + i ,  rowspan = 3,ipady = 33 ) 
                             # ATEND
                      txt0 = ttk.Entry(root2,   width=8)
                      txt0.grid(column=19, row= 5+i ,  rowspan = 3,ipady = 33 )

                                # REMARK
                      txt0 = ttk.Entry(root2,   width=8)
                      txt0.grid(column=20, row= 5+ i ,  rowspan = 3,ipady = 33 ) 
                                # COND
                      txt0 = ttk.Entry(root2,   width=8)
                      txt0.grid(column=21, row= 5+i ,  rowspan = 3,ipady = 33 )
                                # cond
                      txt0 = ttk.Entry(root2,   width=8)
                      txt0.grid(column=22, row= 5 + i ,  rowspan = 3,ipady = 33 )
                      
                      i = i + 3 
                      s= s + 1      
                                #semister
                for xd in range(21):  
                  root.txt0 = ttk.Entry(root2, width=8,font = ("Arial",9, "bold"))
                  root.txt0.grid(column=5, row=xd + 5, ipady =4) 
                  if xd==0 or xd==3 or xd==6 or xd==9 or xd==12 or xd==15 or xd==18:
                     root.txt0.insert(0, "1st")  
                  if xd==1 or xd==4 or xd==7 or xd==10 or xd==13 or xd==16 or xd==19:
                     root.txt0.insert(0, "2nd")
                  if xd==2 or xd==5 or xd==8 or xd==11 or xd==14 or xd==17 or xd==20:
                     root.txt0.insert(0, "Avrg")
         
                                #crateing the entry box

                root.stu3M = []
                for xd in range(21):
                    for dx in range(14):  
                          stu1 = ttk.Entry(root2, width=8)
                          stu1.grid(column=dx +6, row=xd + 5, ipady =4)         
                          root.stu3M.append(stu1)
                          stu1.insert(0,'0')
                          
                
                  #Buttones
                root.btn = ttk.Button(root2, text = 'Add1', command=root.Add)
                root.btn.grid(column=1, row=27, columnspan = 2)                
                root.btn = ttk.Button(root2, text = "next page", command=root.Next_page3)
                root.btn.grid(column=19, row=27, columnspan = 4) 
                root2.mainloop()  
                
            
        def Next_page3(root):
                root3 = Tk()
                root3.title('Page -4')
                
                root.intro = Label(root3, text = "MOTTA GENERAL SECONDARY SCHOOL ROSTER", font = ("Arial", 10)) 
                root.intro.grid(column = 0, row = 0, columnspan = 10)
                root.year = Label(root3, text = "YEAR...........................................", font = ("Arial", 10)) 
                root. year.grid(column = 0, row = 1,columnspan = 15)
                root. gread = Label(root3, text = "GR............................................", font = ("Arial", 10)) 
                root. gread.grid(column = 2, row = 1,columnspan = 15)
                root.section = Label(root3, text = "SECTION..................................", font = ("Arial", 10)) 
                root.section.grid(column = 3, row = 1,columnspan = 35)
                root. nam1 = Label(root3, text = "1st H.R.T Name.................................................................SIG................................................................", font = ("Arial", 10)) 
                root.nam1.grid(column = 1, row = 27, columnspan = 20)
                root.nam1 = Label(root3, text = "2nd H.R.T Name..........................................................SIG............DIRECTOR'S NAME:- EWUNETIE ADDIS.SIG.....................", font = ("Arial", 10)) 
                root. nam1.grid(column = 2, row = 28, columnspan = 20)
              
                root.txt1 = Label(root3, text = ".",width=5)
                root.txt1.grid(column=0, row=4)

                root.txt2 = ttk.Entry(root3,  width=3,font = ("Arial",8, "bold"))
                root.txt2.grid(column=1, row=4)
                root.txt2.insert(0,'No')
                root.txt3 = ttk.Entry(root3,  width=20,font = ("Arial",8,"bold"))
                root.txt3.grid(column=2, row=4)
                root.txt3.insert(0,'NAME')
                root.txt4 = ttk.Entry(root3,  width=6,font = ("Arial",8, "bold"))
                root.txt4.grid(column=3, row=4)
                root.txt4.insert(0,'SEX')
                root.txt5 = ttk.Entry(root3, width=6,font = ("Arial",8, "bold"))
                root.txt5.grid(column=4, row=4)
                root.txt5.insert(0,'AGE')
                root.txt6 = ttk.Entry(root3,  width=8,font = ("Arial",8, "bold"))
                root.txt6.grid(column=5, row=4)
                root.txt6.insert(0,'SEM')
                root.txt7 = ttk.Entry(root3,  width=8,font = ("Arial",8, "bold"))
                root.txt7.grid(column=6, row=4)
                root.txt7.insert(0,'AM')
                root.txt8 = ttk.Entry(root3,  width=8,font = ("Arial",8, "bold"))
                root.txt8.grid(column=7, row=4)
                root.txt8.insert(0,'EN')
                root.txt9 = ttk.Entry(root3,  width=8,font = ("Arial",8, "bold"))
                root.txt9.grid(column=8, row=4)
                root.txt9.insert(0,'MA')
                root.txt10 = ttk.Entry(root3,  width=8,font = ("Arial",8, "bold"))
                root.txt10.grid(column=9, row=4)
                root.txt10.insert(0,'PH')
                root.txt11 = ttk.Entry(root3,  width=8,font = ("Arial",8, "bold"))
                root.txt11.grid(column=10, row=4)
                root.txt11.insert(0,'CH')
                root.txt12 = ttk.Entry(root3,  width=8,font = ("Arial",8, "bold"))
                root.txt12.grid(column=11, row=4)
                root.txt12.insert(0,'BI')
                root.txt13 = ttk.Entry(root3,  width=8,font = ("Arial",8, "bold"))
                root.txt13.grid(column=12, row=4)
                root.txt13.insert(0,'GI')
                root.txt14 = ttk.Entry(root3,  width=8,font = ("Arial",8, "bold"))
                root.txt14.grid(column=13, row=4)
                root.txt14.insert(0,'HI')
                root.txt15 = ttk.Entry(root3,  width=8,font = ("Arial",8, "bold"))
                root.txt15.grid(column=14, row=4)
                root.txt15.insert(0,'CV')
                root.txt16 = ttk.Entry(root3,  width=8,font = ("Arial",8, "bold"))
                root.txt16.grid(column=15, row=4)
                root.txt16.insert(0,'HP')
                root.txt16 = ttk.Entry(root3,  width=8,font = ("Arial",8, "bold"))
                root.txt16.grid(column=16, row=4)
                root.txt16.insert(0,'IT')
                root.txt17 = ttk.Entry(root3,  width=8,font = ("Arial",8, "bold"))
                root.txt17.grid(column=17, row=4)
                root.txt17.insert(0,'SUM')
                root.txt18 = ttk.Entry(root3,  width=8,font = ("Arial",8, "bold"))
                root.txt18.grid(column=18, row=4)
                root.txt18.insert(0,'AVRG')
                root.txt19 = ttk.Entry(root3,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=19, row=4)
                root.txt19.insert(0,'RANK')
                root.txt19 = ttk.Entry(root3,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=20, row=4)
                root.txt19.insert(0,'ATEND')
                root.txt19 = ttk.Entry(root3,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=21, row=4)
                root.txt19.insert(0,'COND')
                root.txt19 = ttk.Entry(root3,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=22, row=4)
                root.txt19.insert(0,'RMARK')


                                 #sex
                root.sex22= ttk.Entry(root3,   width=6)
                root.sex22.grid(column=3, row= 5 ,  rowspan = 3,ipady = 33 ) 

                root.sex23= ttk.Entry(root3,   width=6)
                root.sex23.grid(column=3, row= 8 ,  rowspan = 3,ipady = 33 ) 
                
                root.sex24 = ttk.Entry(root3,   width=6)
                root.sex24.grid(column=3, row= 11 ,  rowspan = 3,ipady = 33 )

                root.sex25 = ttk.Entry(root3,   width=6)
                root.sex25.grid(column=3, row= 14 ,  rowspan = 3,ipady = 33 )

                root.sex26 = ttk.Entry(root3,   width=6)
                root.sex26.grid(column=3, row= 17 ,  rowspan = 3,ipady = 33 )

                root.sex27= ttk.Entry(root3,   width=6)
                root.sex27.grid(column=3, row= 20 ,  rowspan = 3,ipady = 33 )

                root.sex28= ttk.Entry(root3,   width=6)
                root.sex28.grid(column=3, row= 23 ,  rowspan = 3,ipady = 33 )


                        #number
                i = 0
                s= 22
                while i <= 20 and s<= 30:                
                      root.txt0 = ttk.Entry(root3, width=3)
                      root.txt0.grid(column=1, row=5+i  ,rowspan = 3,ipady = 33)
                      root.txt0.insert(0, s)
                              #name
                      root.txt0 = tk.Text(root3, height =1,width=15)
                      root.txt0.grid(column=2, row = 5+i,rowspan = 3,ipady = 33)  
                              
                              #Age                  
                      root.txt0 = ttk.Entry(root3,   width=6)
                      root.txt0.grid(column=4, row= 5  + i ,  rowspan = 3,ipady = 33 ) 
                             # ATEND
                      txt0 = ttk.Entry(root3,   width=8)
                      txt0.grid(column=19, row= 5+i ,  rowspan = 3,ipady = 33 )

                                # REMARK
                      txt0 = ttk.Entry(root3,   width=8)
                      txt0.grid(column=20, row= 5+ i ,  rowspan = 3,ipady = 33 ) 
                                # COND
                      txt0 = ttk.Entry(root3,   width=8)
                      txt0.grid(column=21, row= 5+i ,  rowspan = 3,ipady = 33 )
                                # cond
                      txt0 = ttk.Entry(root3,   width=8)
                      txt0.grid(column=22, row= 5 + i ,  rowspan = 3,ipady = 33 )
                      
                      i = i + 3 
                      s= s + 1      
                                #semister
                for xd in range(21):  
                  root.txt0 = ttk.Entry(root3, width=8,font = ("Arial",9, "bold"))
                  root.txt0.grid(column=5, row=xd + 5, ipady =4) 
                  if xd==0 or xd==3 or xd==6 or xd==9 or xd==12 or xd==15 or xd==18:
                     root.txt0.insert(0, "1st")  
                  if xd==1 or xd==4 or xd==7 or xd==10 or xd==13 or xd==16 or xd==19:
                     root.txt0.insert(0, "2nd")
                  if xd==2 or xd==5 or xd==8 or xd==11 or xd==14 or xd==17 or xd==20:
                     root.txt0.insert(0, "Avrg")
         
                                #crateing the entry box

                root.stu4M = []
                for xd in range(21):
                    for dx in range(14):  
                          stu1 = ttk.Entry(root3, width=8)
                          stu1.grid(column=dx +6, row=xd + 5, ipady =4)         
                          root.stu4M.append(stu1)
                          stu1.insert(0,'0')
                          
                
                  #Buttones
                root.btn = ttk.Button(root3, text = 'Add1', command=root.Add)
                root.btn.grid(column=1, row=27, columnspan = 2)                
                root.btn = ttk.Button(root3, text = "next page", command=root.Next_page4)
                root.btn.grid(column=19, row=27, columnspan = 4) 
                root3.mainloop()    
                
            
            
        def Next_page4(root):
                root4 = Tk()
                root4.title('Page -5')
                root.intro = Label(root4, text = "MOTTA GENERAL SECONDARY SCHOOL ROSTER", font = ("Arial", 10)) 
                root.intro.grid(column = 0, row = 0, columnspan = 10)
                root.year = Label(root4, text = "YEAR...........................................", font = ("Arial", 10)) 
                root. year.grid(column = 0, row = 1,columnspan = 15)
                root. gread = Label(root4, text = "GR............................................", font = ("Arial", 10)) 
                root. gread.grid(column = 2, row = 1,columnspan = 15)
                root.section = Label(root4, text = "SECTION..................................", font = ("Arial", 10)) 
                root.section.grid(column = 3, row = 1,columnspan = 35)
                root. nam1 = Label(root4, text = "1st H.R.T Name.................................................................SIG................................................................", font = ("Arial", 10)) 
                root.nam1.grid(column = 1, row = 27, columnspan = 20)
                root.nam1 = Label(root4, text = "2nd H.R.T Name..........................................................SIG............DIRECTOR'S NAME:- EWUNETIE ADDIS.SIG.....................", font = ("Arial", 10)) 
                root. nam1.grid(column = 2, row = 28, columnspan = 20)
              
                root.txt1 = Label(root4, text = ".",width=5)
                root.txt1.grid(column=0, row=4)

                root.txt2 = ttk.Entry(root4,  width=3,font = ("Arial",8, "bold"))
                root.txt2.grid(column=1, row=4)
                root.txt2.insert(0,'No')
                root.txt3 = ttk.Entry(root4,  width=20,font = ("Arial",8,"bold"))
                root.txt3.grid(column=2, row=4)
                root.txt3.insert(0,'NAME')
                root.txt4 = ttk.Entry(root4,  width=6,font = ("Arial",8, "bold"))
                root.txt4.grid(column=3, row=4)
                root.txt4.insert(0,'SEX')
                root.txt5 = ttk.Entry(root4, width=6,font = ("Arial",8, "bold"))
                root.txt5.grid(column=4, row=4)
                root.txt5.insert(0,'AGE')
                root.txt6 = ttk.Entry(root4,  width=8,font = ("Arial",8, "bold"))
                root.txt6.grid(column=5, row=4)
                root.txt6.insert(0,'SEM')
                root.txt7 = ttk.Entry(root4,  width=8,font = ("Arial",8, "bold"))
                root.txt7.grid(column=6, row=4)
                root.txt7.insert(0,'AM')
                root.txt8 = ttk.Entry(root4,  width=8,font = ("Arial",8, "bold"))
                root.txt8.grid(column=7, row=4)
                root.txt8.insert(0,'EN')
                root.txt9 = ttk.Entry(root4,  width=8,font = ("Arial",8, "bold"))
                root.txt9.grid(column=8, row=4)
                root.txt9.insert(0,'MA')
                root.txt10 = ttk.Entry(root4,  width=8,font = ("Arial",8, "bold"))
                root.txt10.grid(column=9, row=4)
                root.txt10.insert(0,'PH')
                root.txt11 = ttk.Entry(root4,  width=8,font = ("Arial",8, "bold"))
                root.txt11.grid(column=10, row=4)
                root.txt11.insert(0,'CH')
                root.txt12 = ttk.Entry(root4,  width=8,font = ("Arial",8, "bold"))
                root.txt12.grid(column=11, row=4)
                root.txt12.insert(0,'BI')
                root.txt13 = ttk.Entry(root4,  width=8,font = ("Arial",8, "bold"))
                root.txt13.grid(column=12, row=4)
                root.txt13.insert(0,'GI')
                root.txt14 = ttk.Entry(root4,  width=8,font = ("Arial",8, "bold"))
                root.txt14.grid(column=13, row=4)
                root.txt14.insert(0,'HI')
                root.txt15 = ttk.Entry(root4,  width=8,font = ("Arial",8, "bold"))
                root.txt15.grid(column=14, row=4)
                root.txt15.insert(0,'CV')
                root.txt16 = ttk.Entry(root4,  width=8,font = ("Arial",8, "bold"))
                root.txt16.grid(column=15, row=4)
                root.txt16.insert(0,'HP')
                root.txt16 = ttk.Entry(root4,  width=8,font = ("Arial",8, "bold"))
                root.txt16.grid(column=16, row=4)
                root.txt16.insert(0,'IT')
                root.txt17 = ttk.Entry(root4,  width=8,font = ("Arial",8, "bold"))
                root.txt17.grid(column=17, row=4)
                root.txt17.insert(0,'SUM')
                root.txt18 = ttk.Entry(root4,  width=8,font = ("Arial",8, "bold"))
                root.txt18.grid(column=18, row=4)
                root.txt18.insert(0,'AVRG')
                root.txt19 = ttk.Entry(root4,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=19, row=4)
                root.txt19.insert(0,'RANK')
                root.txt19 = ttk.Entry(root4,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=20, row=4)
                root.txt19.insert(0,'ATEND')
                root.txt19 = ttk.Entry(root4,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=21, row=4)
                root.txt19.insert(0,'COND')
                root.txt19 = ttk.Entry(root4,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=22, row=4)
                root.txt19.insert(0,'RMARK')

                                 #sex
                root.sex29= ttk.Entry(root4,   width=6)
                root.sex29.grid(column=3, row= 5 ,  rowspan = 3,ipady = 33 ) 

                root.sex30= ttk.Entry(root4,   width=6)
                root.sex30.grid(column=3, row= 8 ,  rowspan = 3,ipady = 33 ) 
                
                root.sex31 = ttk.Entry(root4,   width=6)
                root.sex31.grid(column=3, row= 11 ,  rowspan = 3,ipady = 33 )

                root.sex32 = ttk.Entry(root4,   width=6)
                root.sex32.grid(column=3, row= 14 ,  rowspan = 3,ipady = 33 )

                root.sex33 = ttk.Entry(root4,   width=6)
                root.sex33.grid(column=3, row= 17 ,  rowspan = 3,ipady = 33 )

                root.sex34= ttk.Entry(root4,   width=6)
                root.sex34.grid(column=3, row= 20 ,  rowspan = 3,ipady = 33 )

                root.sex35= ttk.Entry(root4,   width=6)
                root.sex35.grid(column=3, row= 23 ,  rowspan = 3,ipady = 33 )




                        #number
                i = 0
                s= 29
                while i <= 20 and s<= 39:                
                      root.txt0 = ttk.Entry(root4, width=3)
                      root.txt0.grid(column=1, row=5+i  ,rowspan = 3,ipady = 33)
                      root.txt0.insert(0, s)
                              #name
                      root.txt0 = tk.Text(root4, height =1,width=15)
                      root.txt0.grid(column=2, row = 5+i,rowspan = 3,ipady = 33)  
                            
                              #Age                  
                      root.txt0 = ttk.Entry(root4,   width=6)
                      root.txt0.grid(column=4, row= 5  + i ,  rowspan = 3,ipady = 33 ) 
                             # ATEND
                      txt0 = ttk.Entry(root4,   width=8)
                      txt0.grid(column=19, row= 5+i ,  rowspan = 3,ipady = 33 )

                                # REMARK
                      txt0 = ttk.Entry(root4,   width=8)
                      txt0.grid(column=20, row= 5+ i ,  rowspan = 3,ipady = 33 ) 
                                # COND
                      txt0 = ttk.Entry(root4,   width=8)
                      txt0.grid(column=21, row= 5+i ,  rowspan = 3,ipady = 33 )
                                # cond
                      txt0 = ttk.Entry(root4,   width=8)
                      txt0.grid(column=22, row= 5 + i ,  rowspan = 3,ipady = 33 )
                      
                      i = i + 3 
                      s= s + 1      
                                #semister
                for xd in range(21):  
                  root.txt0 = ttk.Entry(root4, width=8,font = ("Arial",9, "bold"))
                  root.txt0.grid(column=5, row=xd + 5, ipady =4) 
                  if xd==0 or xd==3 or xd==6 or xd==9 or xd==12 or xd==15 or xd==18:
                     root.txt0.insert(0, "1st")  
                  if xd==1 or xd==4 or xd==7 or xd==10 or xd==13 or xd==16 or xd==19:
                     root.txt0.insert(0, "2nd")
                  if xd==2 or xd==5 or xd==8 or xd==11 or xd==14 or xd==17 or xd==20:
                     root.txt0.insert(0, "Avrg")
         
                                #crateing the entry box

                root.stu5M = []
                for xd in range(21):
                    for dx in range(14):  
                          stu1 = ttk.Entry(root4, width=8)
                          stu1.grid(column=dx +6, row=xd + 5, ipady =4)         
                          root.stu5M.append(stu1)
                          stu1.insert(0,'0')
                          
                
                  #Buttones
                root.btn = ttk.Button(root4, text = 'Add1', command=root.Add)
                root.btn.grid(column=1, row=27, columnspan = 2)                
                root.btn = ttk.Button(root4, text = "next page", command=root.Next_page5)
                root.btn.grid(column=19, row=27, columnspan = 4) 
                root4.mainloop()       
                
         
        def Next_page5(root):
                root5 = Tk()
                root5.title('Page -6')
                root.intro = Label(root5, text = "MOTTA GENERAL SECONDARY SCHOOL ROSTER", font = ("Arial", 10)) 
                root.intro.grid(column = 0, row = 0, columnspan = 10)
                root.year = Label(root5, text = "YEAR...........................................", font = ("Arial", 10)) 
                root. year.grid(column = 0, row = 1,columnspan = 15)
                root. gread = Label(root5, text = "GR............................................", font = ("Arial", 10)) 
                root. gread.grid(column = 2, row = 1,columnspan = 15)
                root.section = Label(root5, text = "SECTION..................................", font = ("Arial", 10)) 
                root.section.grid(column = 3, row = 1,columnspan = 35)
                root. nam1 = Label(root5, text = "1st H.R.T Name.................................................................SIG................................................................", font = ("Arial", 10)) 
                root.nam1.grid(column = 1, row = 27, columnspan = 20)
                root.nam1 = Label(root5, text = "2nd H.R.T Name..........................................................SIG............DIRECTOR'S NAME:- EWUNETIE ADDIS.SIG.....................", font = ("Arial", 10)) 
                root. nam1.grid(column = 2, row = 28, columnspan = 20)
              
                root.txt1 = Label(root5, text = ".",width=5)
                root.txt1.grid(column=0, row=4)

                root.txt2 = ttk.Entry(root5,  width=3,font = ("Arial",8, "bold"))
                root.txt2.grid(column=1, row=4)
                root.txt2.insert(0,'No')
                root.txt3 = ttk.Entry(root5,  width=20,font = ("Arial",8,"bold"))
                root.txt3.grid(column=2, row=4)
                root.txt3.insert(0,'NAME')
                root.txt4 = ttk.Entry(root5,  width=6,font = ("Arial",8, "bold"))
                root.txt4.grid(column=3, row=4)
                root.txt4.insert(0,'SEX')
                root.txt5 = ttk.Entry(root5, width=6,font = ("Arial",8, "bold"))
                root.txt5.grid(column=4, row=4)
                root.txt5.insert(0,'AGE')
                root.txt6 = ttk.Entry(root5,  width=8,font = ("Arial",8, "bold"))
                root.txt6.grid(column=5, row=4)
                root.txt6.insert(0,'SEM')
                root.txt7 = ttk.Entry(root5,  width=8,font = ("Arial",8, "bold"))
                root.txt7.grid(column=6, row=4)
                root.txt7.insert(0,'AM')
                root.txt8 = ttk.Entry(root5,  width=8,font = ("Arial",8, "bold"))
                root.txt8.grid(column=7, row=4)
                root.txt8.insert(0,'EN')
                root.txt9 = ttk.Entry(root5,  width=8,font = ("Arial",8, "bold"))
                root.txt9.grid(column=8, row=4)
                root.txt9.insert(0,'MA')
                root.txt10 = ttk.Entry(root5,  width=8,font = ("Arial",8, "bold"))
                root.txt10.grid(column=9, row=4)
                root.txt10.insert(0,'PH')
                root.txt11 = ttk.Entry(root5,  width=8,font = ("Arial",8, "bold"))
                root.txt11.grid(column=10, row=4)
                root.txt11.insert(0,'CH')
                root.txt12 = ttk.Entry(root5,  width=8,font = ("Arial",8, "bold"))
                root.txt12.grid(column=11, row=4)
                root.txt12.insert(0,'BI')
                root.txt13 = ttk.Entry(root5,  width=8,font = ("Arial",8, "bold"))
                root.txt13.grid(column=12, row=4)
                root.txt13.insert(0,'GI')
                root.txt14 = ttk.Entry(root5,  width=8,font = ("Arial",8, "bold"))
                root.txt14.grid(column=13, row=4)
                root.txt14.insert(0,'HI')
                root.txt15 = ttk.Entry(root5,  width=8,font = ("Arial",8, "bold"))
                root.txt15.grid(column=14, row=4)
                root.txt15.insert(0,'CV')
                root.txt16 = ttk.Entry(root5,  width=8,font = ("Arial",8, "bold"))
                root.txt16.grid(column=15, row=4)
                root.txt16.insert(0,'HP')
                root.txt16 = ttk.Entry(root5,  width=8,font = ("Arial",8, "bold"))
                root.txt16.grid(column=16, row=4)
                root.txt16.insert(0,'IT')
                root.txt17 = ttk.Entry(root5,  width=8,font = ("Arial",8, "bold"))
                root.txt17.grid(column=17, row=4)
                root.txt17.insert(0,'SUM')
                root.txt18 = ttk.Entry(root5,  width=8,font = ("Arial",8, "bold"))
                root.txt18.grid(column=18, row=4)
                root.txt18.insert(0,'AVRG')
                root.txt19 = ttk.Entry(root5,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=19, row=4)
                root.txt19.insert(0,'RANK')
                root.txt19 = ttk.Entry(root5,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=20, row=4)
                root.txt19.insert(0,'ATEND')
                root.txt19 = ttk.Entry(root5,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=21, row=4)
                root.txt19.insert(0,'COND')
                root.txt19 = ttk.Entry(root5,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=22, row=4)
                root.txt19.insert(0,'RMARK')

                                  #sex
                root.sex36= ttk.Entry(root5,   width=6)
                root.sex36.grid(column=3, row= 5 ,  rowspan = 3,ipady = 33 ) 

                root.sex37= ttk.Entry(root5,   width=6)
                root.sex37.grid(column=3, row= 8 ,  rowspan = 3,ipady = 33 ) 
                
                root.sex38 = ttk.Entry(root5,   width=6)
                root.sex38.grid(column=3, row= 11 ,  rowspan = 3,ipady = 33 )

                root.sex39 = ttk.Entry(root5,   width=6)
                root.sex39.grid(column=3, row= 14 ,  rowspan = 3,ipady = 33 )

                root.sex40 = ttk.Entry(root5,   width=6)
                root.sex40.grid(column=3, row= 17 ,  rowspan = 3,ipady = 33 )

                root.sex41= ttk.Entry(root5,   width=6)
                root.sex41.grid(column=3, row= 20 ,  rowspan = 3,ipady = 33 )

                root.sex42= ttk.Entry(root5,   width=6)
                root.sex42.grid(column=3, row= 23 ,  rowspan = 3,ipady = 33 )



                        #number
                i = 0
                s= 36
                while i <= 20 and s<= 43:                
                      root.txt0 = ttk.Entry(root5, width=3)
                      root.txt0.grid(column=1, row=5+i  ,rowspan = 3,ipady = 33)
                      root.txt0.insert(0, s)
                              #name
                      root.txt0 = tk.Text(root5, height =1,width=15)
                      root.txt0.grid(column=2, row = 5+i,rowspan = 3,ipady = 33)  
                              
                              #Age                  
                      root.txt0 = ttk.Entry(root5,   width=6)
                      root.txt0.grid(column=4, row= 5  + i ,  rowspan = 3,ipady = 33 ) 
                             # ATEND
                      txt0 = ttk.Entry(root5,   width=8)
                      txt0.grid(column=19, row= 5+i ,  rowspan = 3,ipady = 33 )

                                # REMARK
                      txt0 = ttk.Entry(root5,   width=8)
                      txt0.grid(column=20, row= 5+ i ,  rowspan = 3,ipady = 33 ) 
                                # COND
                      txt0 = ttk.Entry(root5,   width=8)
                      txt0.grid(column=21, row= 5+i ,  rowspan = 3,ipady = 33 )
                                # cond
                      txt0 = ttk.Entry(root5,   width=8)
                      txt0.grid(column=22, row= 5 + i ,  rowspan = 3,ipady = 33 )
                      
                      i = i + 3 
                      s= s + 1      
                                #semister
                for xd in range(21):  
                  root.txt0 = ttk.Entry(root5, width=8,font = ("Arial",9, "bold"))
                  root.txt0.grid(column=5, row=xd + 5, ipady =4) 
                  if xd==0 or xd==3 or xd==6 or xd==9 or xd==12 or xd==15 or xd==18:
                     root.txt0.insert(0, "1st")  
                  if xd==1 or xd==4 or xd==7 or xd==10 or xd==13 or xd==16 or xd==19:
                     root.txt0.insert(0, "2nd")
                  if xd==2 or xd==5 or xd==8 or xd==11 or xd==14 or xd==17 or xd==20:
                     root.txt0.insert(0, "Avrg")
         
                                #crateing the entry box

                root.stu6M = []
                for xd in range(21):
                    for dx in range(14):  
                          stu1 = ttk.Entry(root5, width=8)
                          stu1.grid(column=dx +6, row=xd + 5, ipady =4)         
                          root.stu6M.append(stu1)
                          stu1.insert(0,'0')
                          
                
                  #Buttones
                root.btn = ttk.Button(root5, text = 'Add1', command=root.Add)
                root.btn.grid(column=1, row=27, columnspan = 2)                
                root.btn = ttk.Button(root5, text = "next page", command=root.Next_page7)
                root.btn.grid(column=19, row=27, columnspan = 4) 
                root5.mainloop()  
         
         
        def Next_page7(root):
                root6 = Tk()
                root6.title('Page -7')
                root.intro = Label(root6, text = "MOTTA GENERAL SECONDARY SCHOOL ROSTER", font = ("Arial", 10)) 
                root.intro.grid(column = 0, row = 0, columnspan = 10)
                root.year = Label(root6, text = "YEAR...........................................", font = ("Arial", 10)) 
                root. year.grid(column = 0, row = 1,columnspan = 15)
                root. gread = Label(root6, text = "GR............................................", font = ("Arial", 10)) 
                root. gread.grid(column = 2, row = 1,columnspan = 15)
                root.section = Label(root6, text = "SECTION..................................", font = ("Arial", 10)) 
                root.section.grid(column = 3, row = 1,columnspan = 35)
                root. nam1 = Label(root6, text = "1st H.R.T Name.................................................................SIG................................................................", font = ("Arial", 10)) 
                root.nam1.grid(column = 1, row = 27, columnspan = 20)
                root.nam1 = Label(root6, text = "2nd H.R.T Name..........................................................SIG............DIRECTOR'S NAME:- EWUNETIE ADDIS.SIG.....................", font = ("Arial", 10)) 
                root. nam1.grid(column = 2, row = 28, columnspan = 20)
              
                root.txt1 = Label(root6, text = ".",width=5)
                root.txt1.grid(column=0, row=4)

                root.txt2 = ttk.Entry(root6,  width=3,font = ("Arial",8, "bold"))
                root.txt2.grid(column=1, row=4)
                root.txt2.insert(0,'No')
                root.txt3 = ttk.Entry(root6,  width=20,font = ("Arial",8,"bold"))
                root.txt3.grid(column=2, row=4)
                root.txt3.insert(0,'NAME')
                root.txt4 = ttk.Entry(root6,  width=6,font = ("Arial",8, "bold"))
                root.txt4.grid(column=3, row=4)
                root.txt4.insert(0,'SEX')
                root.txt5 = ttk.Entry(root6, width=6,font = ("Arial",8, "bold"))
                root.txt5.grid(column=4, row=4)
                root.txt5.insert(0,'AGE')
                root.txt6 = ttk.Entry(root6,  width=8,font = ("Arial",8, "bold"))
                root.txt6.grid(column=5, row=4)
                root.txt6.insert(0,'SEM')
                root.txt7 = ttk.Entry(root6,  width=8,font = ("Arial",8, "bold"))
                root.txt7.grid(column=6, row=4)
                root.txt7.insert(0,'AM')
                root.txt8 = ttk.Entry(root6,  width=8,font = ("Arial",8, "bold"))
                root.txt8.grid(column=7, row=4)
                root.txt8.insert(0,'EN')
                root.txt9 = ttk.Entry(root6,  width=8,font = ("Arial",8, "bold"))
                root.txt9.grid(column=8, row=4)
                root.txt9.insert(0,'MA')
                root.txt10 = ttk.Entry(root6,  width=8,font = ("Arial",8, "bold"))
                root.txt10.grid(column=9, row=4)
                root.txt10.insert(0,'PH')
                root.txt11 = ttk.Entry(root6,  width=8,font = ("Arial",8, "bold"))
                root.txt11.grid(column=10, row=4)
                root.txt11.insert(0,'CH')
                root.txt12 = ttk.Entry(root6,  width=8,font = ("Arial",8, "bold"))
                root.txt12.grid(column=11, row=4)
                root.txt12.insert(0,'BI')
                root.txt13 = ttk.Entry(root6,  width=8,font = ("Arial",8, "bold"))
                root.txt13.grid(column=12, row=4)
                root.txt13.insert(0,'GI')
                root.txt14 = ttk.Entry(root6,  width=8,font = ("Arial",8, "bold"))
                root.txt14.grid(column=13, row=4)
                root.txt14.insert(0,'HI')
                root.txt15 = ttk.Entry(root6,  width=8,font = ("Arial",8, "bold"))
                root.txt15.grid(column=14, row=4)
                root.txt15.insert(0,'CV')
                root.txt16 = ttk.Entry(root6,  width=8,font = ("Arial",8, "bold"))
                root.txt16.grid(column=15, row=4)
                root.txt16.insert(0,'HP')
                root.txt16 = ttk.Entry(root6,  width=8,font = ("Arial",8, "bold"))
                root.txt16.grid(column=16, row=4)
                root.txt16.insert(0,'IT')
                root.txt17 = ttk.Entry(root6,  width=8,font = ("Arial",8, "bold"))
                root.txt17.grid(column=17, row=4)
                root.txt17.insert(0,'SUM')
                root.txt18 = ttk.Entry(root6,  width=8,font = ("Arial",8, "bold"))
                root.txt18.grid(column=18, row=4)
                root.txt18.insert(0,'AVRG')
                root.txt19 = ttk.Entry(root6,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=19, row=4)
                root.txt19.insert(0,'RANK')
                root.txt19 = ttk.Entry(root6,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=20, row=4)
                root.txt19.insert(0,'ATEND')
                root.txt19 = ttk.Entry(root6,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=21, row=4)
                root.txt19.insert(0,'COND')
                root.txt19 = ttk.Entry(root6,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=22, row=4)
                root.txt19.insert(0,'RMARK')

                                #sex
                root.sex43= ttk.Entry(root6,   width=6)
                root.sex43.grid(column=3, row= 5 ,  rowspan = 3,ipady = 33 ) 

                root.sex44= ttk.Entry(root6,   width=6)
                root.sex44.grid(column=3, row= 8 ,  rowspan = 3,ipady = 33 ) 
                
                root.sex45 = ttk.Entry(root6,   width=6)
                root.sex45.grid(column=3, row= 11 ,  rowspan = 3,ipady = 33 )

                root.sex46 = ttk.Entry(root6,   width=6)
                root.sex46.grid(column=3, row= 14 ,  rowspan = 3,ipady = 33 )

                root.sex47 = ttk.Entry(root6,   width=6)
                root.sex47.grid(column=3, row= 17 ,  rowspan = 3,ipady = 33 )

                root.sex48= ttk.Entry(root6,   width=6)
                root.sex48.grid(column=3, row= 20 ,  rowspan = 3,ipady = 33 )

                root.sex49= ttk.Entry(root6,   width=6)
                root.sex49.grid(column=3, row= 23 ,  rowspan = 3,ipady = 33 )



                        #number
                i = 0
                s= 43
                while i <= 20 and s<= 50:                
                      root.txt0 = ttk.Entry(root6, width=3)
                      root.txt0.grid(column=1, row=5+i  ,rowspan = 3,ipady = 33)
                      root.txt0.insert(0, s)
                              #name
                      root.txt0 = tk.Text(root6, height =1,width=15)
                      root.txt0.grid(column=2, row = 5+i,rowspan = 3,ipady = 33)  
                              
                              #Age                  
                      root.txt0 = ttk.Entry(root6,   width=6)
                      root.txt0.grid(column=4, row= 5  + i ,  rowspan = 3,ipady = 33 ) 
                             # ATEND
                      txt0 = ttk.Entry(root6,   width=8)
                      txt0.grid(column=19, row= 5+i ,  rowspan = 3,ipady = 33 )

                                # REMARK
                      txt0 = ttk.Entry(root6,   width=8)
                      txt0.grid(column=20, row= 5+ i ,  rowspan = 3,ipady = 33 ) 
                                # COND
                      txt0 = ttk.Entry(root6,   width=8)
                      txt0.grid(column=21, row= 5+i ,  rowspan = 3,ipady = 33 )
                                # cond
                      txt0 = ttk.Entry(root6,   width=8)
                      txt0.grid(column=22, row= 5 + i ,  rowspan = 3,ipady = 33 )
                      
                      i = i + 3 
                      s= s + 1      
                                #semister
                for xd in range(21):  
                  root.txt0 = ttk.Entry(root6, width=8,font = ("Arial",9, "bold"))
                  root.txt0.grid(column=5, row=xd + 5, ipady =4)
                  if xd==0 or xd==3 or xd==6 or xd==9 or xd==12 or xd==15 or xd==18:
                     root.txt0.insert(0, "1st")  
                  if xd==1 or xd==4 or xd==7 or xd==10 or xd==13 or xd==16 or xd==19:
                     root.txt0.insert(0, "2nd")
                  if xd==2 or xd==5 or xd==8 or xd==11 or xd==14 or xd==17 or xd==20:
                     root.txt0.insert(0, "Avrg")
         
                                #crateing the entry box

                root.stu7M = []
                for xd in range(21):
                    for dx in range(14):  
                          stu1 = ttk.Entry(root6, width=8)
                          stu1.grid(column=dx +6, row=xd + 5, ipady =4)         
                          root.stu7M.append(stu1)
                          stu1.insert(0,'0')
               
                
                  #Buttones
                root.btn = ttk.Button(root6, text = 'Add', command=root.Add)
                root.btn.grid(column=1, row=27, columnspan = 2)
                                 
                root.btn = ttk.Button(root6, text = "next page", command=root.Next_page8)
                root.btn.grid(column=19, row=27, columnspan = 4) 
                root6.mainloop()        
        
        def Next_page8(root):
                root7 = Tk()
                root7.title('Page -8')
                root.intro = Label(root7, text = "MOTTA GENERAL SECONDARY SCHOOL ROSTER", font = ("Arial", 10)) 
                root.intro.grid(column = 0, row = 0, columnspan = 10)
                root.year = Label(root7, text = "YEAR...........................................", font = ("Arial", 10)) 
                root. year.grid(column = 0, row = 1,columnspan = 15)
                root. gread = Label(root7, text = "GR............................................", font = ("Arial", 10)) 
                root. gread.grid(column = 2, row = 1,columnspan = 15)
                root.section = Label(root7, text = "SECTION..................................", font = ("Arial", 10)) 
                root.section.grid(column = 3, row = 1,columnspan = 35)
                root. nam1 = Label(root7, text = "1st H.R.T Name.................................................................SIG................................................................", font = ("Arial", 10)) 
                root.nam1.grid(column = 1, row = 27, columnspan = 20)
                root.nam1 = Label(root7, text = "2nd H.R.T Name..........................................................SIG............DIRECTOR'S NAME:- EWUNETIE ADDIS.SIG.....................", font = ("Arial", 10)) 
                root. nam1.grid(column = 2, row = 28, columnspan = 20)
              
                root.txt1 = Label(root7, text = ".",width=5)
                root.txt1.grid(column=0, row=4)

                root.txt2 = ttk.Entry(root7,  width=3,font = ("Arial",8, "bold"))
                root.txt2.grid(column=1, row=4)
                root.txt2.insert(0,'No')
                root.txt3 = ttk.Entry(root7,  width=20,font = ("Arial",8,"bold"))
                root.txt3.grid(column=2, row=4)
                root.txt3.insert(0,'NAME')
                root.txt4 = ttk.Entry(root7,  width=6,font = ("Arial",8, "bold"))
                root.txt4.grid(column=3, row=4)
                root.txt4.insert(0,'SEX')
                root.txt5 = ttk.Entry(root7, width=6,font = ("Arial",8, "bold"))
                root.txt5.grid(column=4, row=4)
                root.txt5.insert(0,'AGE')
                root.txt6 = ttk.Entry(root7,  width=8,font = ("Arial",8, "bold"))
                root.txt6.grid(column=5, row=4)
                root.txt6.insert(0,'SEM')
                root.txt7 = ttk.Entry(root7,  width=8,font = ("Arial",8, "bold"))
                root.txt7.grid(column=6, row=4)
                root.txt7.insert(0,'AM')
                root.txt8 = ttk.Entry(root7,  width=8,font = ("Arial",8, "bold"))
                root.txt8.grid(column=7, row=4)
                root.txt8.insert(0,'EN')
                root.txt9 = ttk.Entry(root7,  width=8,font = ("Arial",8, "bold"))
                root.txt9.grid(column=8, row=4)
                root.txt9.insert(0,'MA')
                root.txt10 = ttk.Entry(root7,  width=8,font = ("Arial",8, "bold"))
                root.txt10.grid(column=9, row=4)
                root.txt10.insert(0,'PH')
                root.txt11 = ttk.Entry(root7,  width=8,font = ("Arial",8, "bold"))
                root.txt11.grid(column=10, row=4)
                root.txt11.insert(0,'CH')
                root.txt12 = ttk.Entry(root7,  width=8,font = ("Arial",8, "bold"))
                root.txt12.grid(column=11, row=4)
                root.txt12.insert(0,'BI')
                root.txt13 = ttk.Entry(root7,  width=8,font = ("Arial",8, "bold"))
                root.txt13.grid(column=12, row=4)
                root.txt13.insert(0,'GI')
                root.txt14 = ttk.Entry(root7,  width=8,font = ("Arial",8, "bold"))
                root.txt14.grid(column=13, row=4)
                root.txt14.insert(0,'HI')
                root.txt15 = ttk.Entry(root7,  width=8,font = ("Arial",8, "bold"))
                root.txt15.grid(column=14, row=4)
                root.txt15.insert(0,'CV')
                root.txt16 = ttk.Entry(root7,  width=8,font = ("Arial",8, "bold"))
                root.txt16.grid(column=15, row=4)
                root.txt16.insert(0,'HP')
                root.txt16 = ttk.Entry(root7,  width=8,font = ("Arial",8, "bold"))
                root.txt16.grid(column=16, row=4)
                root.txt16.insert(0,'IT')
                root.txt17 = ttk.Entry(root7,  width=8,font = ("Arial",8, "bold"))
                root.txt17.grid(column=17, row=4)
                root.txt17.insert(0,'SUM')
                root.txt18 = ttk.Entry(root7,  width=8,font = ("Arial",8, "bold"))
                root.txt18.grid(column=18, row=4)
                root.txt18.insert(0,'AVRG')
                root.txt19 = ttk.Entry(root7,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=19, row=4)
                root.txt19.insert(0,'RANK')
                root.txt19 = ttk.Entry(root7,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=20, row=4)
                root.txt19.insert(0,'ATEND')
                root.txt19 = ttk.Entry(root7,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=21, row=4)
                root.txt19.insert(0,'COND')
                root.txt19 = ttk.Entry(root7,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=22, row=4)
                root.txt19.insert(0,'RMARK')

                                #sex
                root.sex50= ttk.Entry(root7,   width=6)
                root.sex50.grid(column=3, row= 5 ,  rowspan = 3,ipady = 33 ) 

                root.sex51= ttk.Entry(root7,   width=6)
                root.sex51.grid(column=3, row= 8 ,  rowspan = 3,ipady = 33 ) 
                
                root.sex52 = ttk.Entry(root7,   width=6)
                root.sex52.grid(column=3, row= 11 ,  rowspan = 3,ipady = 33 )

                root.sex53 = ttk.Entry(root7,   width=6)
                root.sex53.grid(column=3, row= 14 ,  rowspan = 3,ipady = 33 )

                root.sex54 = ttk.Entry(root7,   width=6)
                root.sex54.grid(column=3, row= 17 ,  rowspan = 3,ipady = 33 )

                root.sex55= ttk.Entry(root7,   width=6)
                root.sex55.grid(column=3, row= 20 ,  rowspan = 3,ipady = 33 )

                root.sex56= ttk.Entry(root7,   width=6)
                root.sex56.grid(column=3, row= 23 ,  rowspan = 3,ipady = 33 )


                        #number
                i = 0
                s= 50
                while i <= 20 and s<= 57:                
                      root.txt0 = ttk.Entry(root7, width=3)
                      root.txt0.grid(column=1, row=5+i  ,rowspan = 3,ipady = 33)
                      root.txt0.insert(0, s)
                              #name
                      root.txt0 = tk.Text(root7, height =1,width=15)
                      root.txt0.grid(column=2, row = 5+i,rowspan = 3,ipady = 33)  
                               
                              #Age                  
                      root.txt0 = ttk.Entry(root7,   width=6)
                      root.txt0.grid(column=4, row= 5  + i ,  rowspan = 3,ipady = 33 ) 
                             # ATEND
                      txt0 = ttk.Entry(root7,   width=8)
                      txt0.grid(column=19, row= 5+i ,  rowspan = 3,ipady = 33 )

                                # REMARK
                      txt0 = ttk.Entry(root7,   width=8)
                      txt0.grid(column=20, row= 5+ i ,  rowspan = 3,ipady = 33 ) 
                                # COND
                      txt0 = ttk.Entry(root7,   width=8)
                      txt0.grid(column=21, row= 5+i ,  rowspan = 3,ipady = 33 )
                                # cond
                      txt0 = ttk.Entry(root7,   width=8)
                      txt0.grid(column=22, row= 5 + i ,  rowspan = 3,ipady = 33 )
                      
                      i = i + 3 
                      s= s + 1      
                                #semister
                for xd in range(21):  
                  root.txt0 = ttk.Entry(root7, width=8,font = ("Arial",9, "bold"))
                  root.txt0.grid(column=5, row=xd + 5, ipady =4)
                  if xd==0 or xd==3 or xd==6 or xd==9 or xd==12 or xd==15 or xd==18:
                     root.txt0.insert(0, "1st")  
                  if xd==1 or xd==4 or xd==7 or xd==10 or xd==13 or xd==16 or xd==19:
                     root.txt0.insert(0, "2nd")
                  if xd==2 or xd==5 or xd==8 or xd==11 or xd==14 or xd==17 or xd==20:
                     root.txt0.insert(0, "Avrg")                  
         
                                #crateing the entry box

                root.stu8M = []
                for xd in range(21):
                    for dx in range(14):  
                          stu1 = ttk.Entry(root7, width=8)
                          stu1.grid(column=dx +6, row=xd + 5, ipady =4)         
                          root.stu8M.append(stu1)
                          stu1.insert(0,'0')
               
                
                  #Buttones
                root.btn = ttk.Button(root7, text = 'Add', command=root.Add)
                root.btn.grid(column=1, row=27, columnspan = 2)
                                 
                root.btn = ttk.Button(root7, text = "next page", command=root.Next_page9)
                root.btn.grid(column=19, row=27, columnspan = 4) 
                root7.mainloop()  
         
        def Next_page9(root):
                root8 = Tk()
                root8.title('Page -9')
                root.intro = Label(root8, text = "MOTTA GENERAL SECONDARY SCHOOL ROSTER", font = ("Arial", 10)) 
                root.intro.grid(column = 0, row = 0, columnspan = 10)
                root.year = Label(root8, text = "YEAR...........................................", font = ("Arial", 10)) 
                root. year.grid(column = 0, row = 1,columnspan = 15)
                root. gread = Label(root8, text = "GR............................................", font = ("Arial", 10)) 
                root. gread.grid(column = 2, row = 1,columnspan = 15)
                root.section = Label(root8, text = "SECTION..................................", font = ("Arial", 10)) 
                root.section.grid(column = 3, row = 1,columnspan = 35)
                root. nam1 = Label(root8, text = "1st H.R.T Name.................................................................SIG................................................................", font = ("Arial", 10)) 
                root.nam1.grid(column = 1, row = 27, columnspan = 20)
                root.nam1 = Label(root8, text = "2nd H.R.T Name..........................................................SIG............DIRECTOR'S NAME:- EWUNETIE ADDIS.SIG.....................", font = ("Arial", 10)) 
                root. nam1.grid(column = 2, row = 28, columnspan = 20)
              
                root.txt1 = Label(root8, text = ".",width=5)
                root.txt1.grid(column=0, row=4)

                root.txt2 = ttk.Entry(root8,  width=3,font = ("Arial",8, "bold"))
                root.txt2.grid(column=1, row=4)
                root.txt2.insert(0,'No')
                root.txt3 = ttk.Entry(root8,  width=20,font = ("Arial",8,"bold"))
                root.txt3.grid(column=2, row=4)
                root.txt3.insert(0,'NAME')
                root.txt4 = ttk.Entry(root8,  width=6,font = ("Arial",8, "bold"))
                root.txt4.grid(column=3, row=4)
                root.txt4.insert(0,'SEX')
                root.txt5 = ttk.Entry(root8, width=6,font = ("Arial",8, "bold"))
                root.txt5.grid(column=4, row=4)
                root.txt5.insert(0,'AGE')
                root.txt6 = ttk.Entry(root8,  width=8,font = ("Arial",8, "bold"))
                root.txt6.grid(column=5, row=4)
                root.txt6.insert(0,'SEM')
                root.txt7 = ttk.Entry(root8,  width=8,font = ("Arial",8, "bold"))
                root.txt7.grid(column=6, row=4)
                root.txt7.insert(0,'AM')
                root.txt8 = ttk.Entry(root8,  width=8,font = ("Arial",8, "bold"))
                root.txt8.grid(column=7, row=4)
                root.txt8.insert(0,'EN')
                root.txt9 = ttk.Entry(root8,  width=8,font = ("Arial",8, "bold"))
                root.txt9.grid(column=8, row=4)
                root.txt9.insert(0,'MA')
                root.txt10 = ttk.Entry(root8,  width=8,font = ("Arial",8, "bold"))
                root.txt10.grid(column=9, row=4)
                root.txt10.insert(0,'PH')
                root.txt11 = ttk.Entry(root8,  width=8,font = ("Arial",8, "bold"))
                root.txt11.grid(column=10, row=4)
                root.txt11.insert(0,'CH')
                root.txt12 = ttk.Entry(root8,  width=8,font = ("Arial",8, "bold"))
                root.txt12.grid(column=11, row=4)
                root.txt12.insert(0,'BI')
                root.txt13 = ttk.Entry(root8,  width=8,font = ("Arial",8, "bold"))
                root.txt13.grid(column=12, row=4)
                root.txt13.insert(0,'GI')
                root.txt14 = ttk.Entry(root8,  width=8,font = ("Arial",8, "bold"))
                root.txt14.grid(column=13, row=4)
                root.txt14.insert(0,'HI')
                root.txt15 = ttk.Entry(root8,  width=8,font = ("Arial",8, "bold"))
                root.txt15.grid(column=14, row=4)
                root.txt15.insert(0,'CV')
                root.txt16 = ttk.Entry(root8,  width=8,font = ("Arial",8, "bold"))
                root.txt16.grid(column=15, row=4)
                root.txt16.insert(0,'HP')
                root.txt16 = ttk.Entry(root8,  width=8,font = ("Arial",8, "bold"))
                root.txt16.grid(column=16, row=4)
                root.txt16.insert(0,'IT')
                root.txt17 = ttk.Entry(root8,  width=8,font = ("Arial",8, "bold"))
                root.txt17.grid(column=17, row=4)
                root.txt17.insert(0,'SUM')
                root.txt18 = ttk.Entry(root8,  width=8,font = ("Arial",8, "bold"))
                root.txt18.grid(column=18, row=4)
                root.txt18.insert(0,'AVRG')
                root.txt19 = ttk.Entry(root8,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=19, row=4)
                root.txt19.insert(0,'RANK')
                root.txt19 = ttk.Entry(root8,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=20, row=4)
                root.txt19.insert(0,'ATEND')
                root.txt19 = ttk.Entry(root8,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=21, row=4)
                root.txt19.insert(0,'COND')
                root.txt19 = ttk.Entry(root8,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=22, row=4)
                root.txt19.insert(0,'RMARK')

                                #sex
                root.sex57= ttk.Entry(root8,   width=6)
                root.sex57.grid(column=3, row= 5 ,  rowspan = 3,ipady = 33 ) 

                root.sex58= ttk.Entry(root8,   width=6)
                root.sex58.grid(column=3, row= 8 ,  rowspan = 3,ipady = 33 ) 
                
                root.sex59 = ttk.Entry(root8,   width=6)
                root.sex59.grid(column=3, row= 11 ,  rowspan = 3,ipady = 33 )

                root.sex60 = ttk.Entry(root8,   width=6)
                root.sex60.grid(column=3, row= 14 ,  rowspan = 3,ipady = 33 )

                root.sex61 = ttk.Entry(root8,   width=6)
                root.sex61.grid(column=3, row= 17 ,  rowspan = 3,ipady = 33 )

                root.sex62= ttk.Entry(root8,   width=6)
                root.sex62.grid(column=3, row= 20 ,  rowspan = 3,ipady = 33 )

                root.sex63= ttk.Entry(root8,   width=6)
                root.sex63.grid(column=3, row= 23 ,  rowspan = 3,ipady = 33 )



                        #number
                i = 0
                s= 57
                while i <= 20 and s<= 64:                
                      root.txt0 = ttk.Entry(root8, width=3)
                      root.txt0.grid(column=1, row=5+i  ,rowspan = 3,ipady = 33)
                      root.txt0.insert(0, s)
                              #name
                      root.txt0 = tk.Text(root8, height =1,width=15)
                      root.txt0.grid(column=2, row = 5+i,rowspan = 3,ipady = 33)  
                              
                              #Age                  
                      root.txt0 = ttk.Entry(root8,   width=6)
                      root.txt0.grid(column=4, row= 5  + i ,  rowspan = 3,ipady = 33 ) 
                             # ATEND
                      txt0 = ttk.Entry(root8,   width=8)
                      txt0.grid(column=19, row= 5+i ,  rowspan = 3,ipady = 33 )

                                # REMARK
                      txt0 = ttk.Entry(root8,   width=8)
                      txt0.grid(column=20, row= 5+ i ,  rowspan = 3,ipady = 33 ) 
                                # COND
                      txt0 = ttk.Entry(root8,   width=8)
                      txt0.grid(column=21, row= 5+i ,  rowspan = 3,ipady = 33 )
                                # cond
                      txt0 = ttk.Entry(root8,   width=8)
                      txt0.grid(column=22, row= 5 + i ,  rowspan = 3,ipady = 33 )
                      
                      i = i + 3 
                      s= s + 1      
                                #semister
                for xd in range(21):  
                  root.txt0 = ttk.Entry(root8, width=8,font = ("Arial",9, "bold"))
                  root.txt0.grid(column=5, row=xd + 5, ipady =4)
                  if xd==0 or xd==3 or xd==6 or xd==9 or xd==12 or xd==15 or xd==18:
                     root.txt0.insert(0, "1st")  
                  if xd==1 or xd==4 or xd==7 or xd==10 or xd==13 or xd==16 or xd==19:
                     root.txt0.insert(0, "2nd")
                  if xd==2 or xd==5 or xd==8 or xd==11 or xd==14 or xd==17 or xd==20:
                     root.txt0.insert(0, "Avrg")                  
         
                                #crateing the entry box

                root.stu9M = []
                for xd in range(21):
                    for dx in range(14):  
                          stu1 = ttk.Entry(root8, width=8)
                          stu1.grid(column=dx +6, row=xd + 5, ipady =4)         
                          root.stu9M.append(stu1)
                          stu1.insert(0,'0')
               
                
                  #Buttones
                root.btn = ttk.Button(root8, text = 'Add', command=root.Add)
                root.btn.grid(column=1, row=27, columnspan = 2)
                                 
                root.btn = ttk.Button(root8, text = "next page", command=root.Next_page10)
                root.btn.grid(column=19, row=27, columnspan = 4) 
                root8.mainloop() 
                
        def Next_page10(root):
                root9 = Tk()
                root9.title('Page -10')
                root.intro = Label(root9, text = "MOTTA GENERAL SECONDARY SCHOOL ROSTER", font = ("Arial", 10)) 
                root.intro.grid(column = 0, row = 0, columnspan = 10)
                root.year = Label(root9, text = "YEAR...........................................", font = ("Arial", 10)) 
                root. year.grid(column = 0, row = 1,columnspan = 15)
                root. gread = Label(root9, text = "GR............................................", font = ("Arial", 10)) 
                root. gread.grid(column = 2, row = 1,columnspan = 15)
                root.section = Label(root9, text = "SECTION..................................", font = ("Arial", 10)) 
                root.section.grid(column = 3, row = 1,columnspan = 35)
                root. nam1 = Label(root9, text = "1st H.R.T Name.................................................................SIG................................................................", font = ("Arial", 10)) 
                root.nam1.grid(column = 1, row = 27, columnspan = 20)
                root.nam1 = Label(root9, text = "2nd H.R.T Name..........................................................SIG............DIRECTOR'S NAME:- EWUNETIE ADDIS.SIG.....................", font = ("Arial", 10)) 
                root. nam1.grid(column = 2, row = 28, columnspan = 20)
              
                root.txt1 = Label(root9, text = ".",width=5)
                root.txt1.grid(column=0, row=4)

                root.txt2 = ttk.Entry(root9,  width=3,font = ("Arial",8, "bold"))
                root.txt2.grid(column=1, row=4)
                root.txt2.insert(0,'No')
                root.txt3 = ttk.Entry(root9,  width=20,font = ("Arial",8,"bold"))
                root.txt3.grid(column=2, row=4)
                root.txt3.insert(0,'NAME')
                root.txt4 = ttk.Entry(root9,  width=6,font = ("Arial",8, "bold"))
                root.txt4.grid(column=3, row=4)
                root.txt4.insert(0,'SEX')
                root.txt5 = ttk.Entry(root9, width=6,font = ("Arial",8, "bold"))
                root.txt5.grid(column=4, row=4)
                root.txt5.insert(0,'AGE')
                root.txt6 = ttk.Entry(root9,  width=8,font = ("Arial",8, "bold"))
                root.txt6.grid(column=5, row=4)
                root.txt6.insert(0,'SEM')
                root.txt7 = ttk.Entry(root9,  width=8,font = ("Arial",8, "bold"))
                root.txt7.grid(column=6, row=4)
                root.txt7.insert(0,'AM')
                root.txt8 = ttk.Entry(root9,  width=8,font = ("Arial",8, "bold"))
                root.txt8.grid(column=7, row=4)
                root.txt8.insert(0,'EN')
                root.txt9 = ttk.Entry(root9,  width=8,font = ("Arial",8, "bold"))
                root.txt9.grid(column=8, row=4)
                root.txt9.insert(0,'MA')
                root.txt10 = ttk.Entry(root9,  width=8,font = ("Arial",8, "bold"))
                root.txt10.grid(column=9, row=4)
                root.txt10.insert(0,'PH')
                root.txt11 = ttk.Entry(root9,  width=8,font = ("Arial",8, "bold"))
                root.txt11.grid(column=10, row=4)
                root.txt11.insert(0,'CH')
                root.txt12 = ttk.Entry(root9,  width=8,font = ("Arial",8, "bold"))
                root.txt12.grid(column=11, row=4)
                root.txt12.insert(0,'BI')
                root.txt13 = ttk.Entry(root9,  width=8,font = ("Arial",8, "bold"))
                root.txt13.grid(column=12, row=4)
                root.txt13.insert(0,'GI')
                root.txt14 = ttk.Entry(root9,  width=8,font = ("Arial",8, "bold"))
                root.txt14.grid(column=13, row=4)
                root.txt14.insert(0,'HI')
                root.txt15 = ttk.Entry(root9,  width=8,font = ("Arial",8, "bold"))
                root.txt15.grid(column=14, row=4)
                root.txt15.insert(0,'CV')
                root.txt16 = ttk.Entry(root9,  width=8,font = ("Arial",8, "bold"))
                root.txt16.grid(column=15, row=4)
                root.txt16.insert(0,'HP')
                root.txt16 = ttk.Entry(root9,  width=8,font = ("Arial",8, "bold"))
                root.txt16.grid(column=16, row=4)
                root.txt16.insert(0,'IT')
                root.txt17 = ttk.Entry(root9,  width=8,font = ("Arial",8, "bold"))
                root.txt17.grid(column=17, row=4)
                root.txt17.insert(0,'SUM')
                root.txt18 = ttk.Entry(root9,  width=8,font = ("Arial",8, "bold"))
                root.txt18.grid(column=18, row=4)
                root.txt18.insert(0,'AVRG')
                root.txt19 = ttk.Entry(root9,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=19, row=4)
                root.txt19.insert(0,'RANK')
                root.txt19 = ttk.Entry(root9,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=20, row=4)
                root.txt19.insert(0,'ATEND')
                root.txt19 = ttk.Entry(root9,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=21, row=4)
                root.txt19.insert(0,'COND')
                root.txt19 = ttk.Entry(root9,  width=8,font = ("Arial",8, "bold"))
                root.txt19.grid(column=22, row=4)
                root.txt19.insert(0,'RMARK')

                                #sex
                root.sex64= ttk.Entry(root9,   width=6)
                root.sex64.grid(column=3, row= 5 ,  rowspan = 3,ipady = 33 ) 

                root.sex65 = ttk.Entry(root9,   width=6)
                root.sex65.grid(column=3, row= 8 ,  rowspan = 3,ipady = 33 ) 
                
                root.sex66 = ttk.Entry(root9,   width=6)
                root.sex66.grid(column=3, row= 11 ,  rowspan = 3,ipady = 33 )

                root.sex67 = ttk.Entry(root9,   width=6)
                root.sex67.grid(column=3, row= 14 ,  rowspan = 3,ipady = 33 )

                root.sex68 = ttk.Entry(root9,   width=6)
                root.sex68.grid(column=3, row= 17 ,  rowspan = 3,ipady = 33 )

                root.sex69 = ttk.Entry(root9,   width=6)
                root.sex69.grid(column=3, row= 20 ,  rowspan = 3,ipady = 33 )

                root.sex70 = ttk.Entry(root9,   width=6)
                root.sex70.grid(column=3, row= 23 ,  rowspan = 3,ipady = 33 )


                        #number
                i = 0
                s= 64
                while i <= 20 and s<= 70:                
                      root.txt0 = ttk.Entry(root9, width=3)
                      root.txt0.grid(column=1, row=5+i  ,rowspan = 3,ipady = 33)
                      root.txt0.insert(0, s)
                              #name
                      root.txt0 = tk.Text(root9, height =1,width=15)
                      root.txt0.grid(column=2, row = 5+i,rowspan = 3,ipady = 33)  
                              
                              #Age                  
                      root.txt0 = ttk.Entry(root9,   width=6)
                      root.txt0.grid(column=4, row= 5  + i ,  rowspan = 3,ipady = 33 ) 
                             # ATEND
                      txt0 = ttk.Entry(root9,   width=8)
                      txt0.grid(column=19, row= 5+i ,  rowspan = 3,ipady = 33 )

                                # REMARK
                      txt0 = ttk.Entry(root9,   width=8)
                      txt0.grid(column=20, row= 5+ i ,  rowspan = 3,ipady = 33 ) 
                                # COND
                      txt0 = ttk.Entry(root9,   width=8)
                      txt0.grid(column=21, row= 5+i ,  rowspan = 3,ipady = 33 )
                                # cond
                      txt0 = ttk.Entry(root9,   width=8)
                      txt0.grid(column=22, row= 5 + i ,  rowspan = 3,ipady = 33 )
                      
                      i = i + 3 
                      s= s + 1      
                                #semister
                for xd in range(21):  
                  root.txt0 = ttk.Entry(root9, width=8,font = ("Arial",9, "bold"))
                  root.txt0.grid(column=5, row=xd + 5, ipady =4) 
                  if xd==0 or xd==3 or xd==6 or xd==9 or xd==12 or xd==15 or xd==18:
                     root.txt0.insert(0, "1st")  
                  if xd==1 or xd==4 or xd==7 or xd==10 or xd==13 or xd==16 or xd==19:
                     root.txt0.insert(0, "2nd")
                  if xd==2 or xd==5 or xd==8 or xd==11 or xd==14 or xd==17 or xd==20:
                     root.txt0.insert(0, "Avrg")
         
                                #crateing the entry box

                root.stu10M = []
                for xd in range(21):
                    for dx in range(14):  
                          stu1 = ttk.Entry(root9, width=8)
                          stu1.grid(column=dx +6, row=xd + 5, ipady =4)         
                          root.stu10M.append(stu1)
                          stu1.insert(0,'0')
               
                
                  #Buttones
                root.btn = ttk.Button(root9, text = 'Add', command=root.Add)
                root.btn.grid(column=1, row=27, columnspan = 2)
                root.btn = ttk.Button(root9, text = "2nd-sem Filter", command=root.filter2)
                root.btn.grid(column=19, row=27, columnspan = 4) 
                root.btn = ttk.Button(root9, text = "1st-sem Filter", command=root.filter)
                root.btn.grid(column=17, row=27, columnspan = 4)                 
                
                root9.mainloop()  
                     
                     #Filter
                     
        def filter(root):
                root10 = Tk()
                root10.title('1st Semester filter')
                #root.intro = Label(root10, text = "MOTTA GENERAL SECONDARY SCHOOL ROSTER", font = ("Arial", 10)) 
                #root.intro.grid(column = 0, row = 0, columnspan = 10)
                root.year = Label(root10, text = "YEAR...........................................", font = ("Arial", 10)) 
                root. year.grid(column = 0, row = 1,columnspan = 15)
                root. gread = Label(root10, text = "GR............................................", font = ("Arial", 10)) 
                root. gread.grid(column = 2, row = 1,columnspan = 15)
                root.section = Label(root10, text = "SECTION..................................", font = ("Arial", 10)) 
                root.section.grid(column = 3, row = 1,columnspan = 35)
                root. nam1 = Label(root10, text = "1st H.R.T Name.................................................................SIG................................................................", font = ("Arial", 10)) 
                root.nam1.grid(column = 1, row = 27, columnspan = 20)
                root.nam1 = Label(root10, text = "2nd H.R.T Name..........................................................SIG............DIRECTOR'S NAME:- EWUNETIE ADDIS.SIG.....................", font = ("Arial", 10)) 
                root. nam1.grid(column = 2, row = 28, columnspan = 20)
                 
                root.txt7 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt7.grid(column=6, row=4)
                root.txt7.insert(0,'AM')
                root.txt8 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt8.grid(column=7, row=4)
                root.txt8.insert(0,'EN')
                root.txt9 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt9.grid(column=8, row=4)
                root.txt9.insert(0,'MA')
                root.txt10 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt10.grid(column=9, row=4)
                root.txt10.insert(0,'PH')
                root.txt11 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt11.grid(column=10, row=4)
                root.txt11.insert(0,'CH')
                root.txt12 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt12.grid(column=11, row=4)
                root.txt12.insert(0,'BI')
                root.txt13 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt13.grid(column=12, row=4)
                root.txt13.insert(0,'GI')
                root.txt14 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt14.grid(column=13, row=4)
                root.txt14.insert(0,'HI')
                root.txt15 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt15.grid(column=14, row=4)
                root.txt15.insert(0,'CV')
                root.txt16 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt16.grid(column=15, row=4)
                root.txt16.insert(0,'HP')
                root.txt16 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt16.grid(column=16, row=4)
                root.txt16.insert(0,'IT')
                root.txt1 = Label(root10, text = ".",width=5)
                root.txt1.grid(column=0, row=4)  
                
                root.txt17 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt17.grid(column=5, row=5, ipady = 8)
                root.txt17.insert(0, '0-49')
                
                root.txt18 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt18.grid(column=5, row=6, ipady = 8)
                root.txt18.insert(0, 'M')
                
                root.txt19 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt19.grid(column=5, row=7, ipady = 8)
                root.txt19.insert(0, 'F')
                
                root.txt20 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt20.grid(column=5, row=8, ipady = 8)
                root.txt20.insert(0, '%')
                
                root.txt21 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt21.grid(column=5, row=9, ipady = 8)
                root.txt21.insert(0, '50-100')
                
                root.txt22 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt22.grid(column=5, row=10, ipady = 8)
                root.txt22.insert(0, 'M')
                
                root.txt23 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt23.grid(column=5, row=11, ipady = 8)
                root.txt23.insert(0, 'F')
                
                root.txt24 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt24.grid(column=5, row=12, ipady = 8)
                root.txt24.insert(0, '%')
                
                root.txt25 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt25.grid(column=5, row=13, ipady = 8)
                root.txt25.insert(0, '75-100')
                
                root.txt26 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt26.grid(column=5, row=14, ipady = 8)
                root.txt26.insert(0, 'M')
                
                root.txt27 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt27.grid(column=5, row=15, ipady = 8)
                root.txt27.insert(0, 'F')
                
                root.txt28 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt28.grid(column=5, row=16, ipady = 8)
                root.txt28.insert(0, '%')

                root.txt29 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt29.grid(column=5, row=17, ipady = 8)
                root.txt29.insert(0, '85-100')
                
                root.txt30 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt30.grid(column=5, row=18, ipady = 8)
                root.txt30.insert(0, 'M')
                
                root.txt31 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt31.grid(column=5, row=19, ipady = 8)
                root.txt31.insert(0, 'F')
                
                root.txt32 = ttk.Entry(root10,  width=8,font = ("Arial",11, "bold"))
                root.txt32.grid(column=5, row=20, ipady = 8)
                root.txt32.insert(0, '%')
                
                root.num = []
                for x in range(11):
                    for i in range(16):
                       
                       tt = ttk.Entry(root10,  width = 10,font = ("Arial",11,))
                       tt.grid(row = 5+i, column = 6+x,ipady = 8)
                       root.num.append(tt)

                root.per = Label(root10, text = "Pleas Enter number of students", font = ("Arial, 11"))
                root.per.grid(column = 22, row = 5, columnspan = 6)
                
                root.per1 = ttk.Entry(root10, width = 7)
                root.per1.grid(column= 22, row = 6 )
                
                root.per2 = ttk. Button(root10, text= "oK", command = root.Add2)
                root.per2.grid(column= 22, row = 7)
                
                  

                                 
                
                root10.mainloop() 
    
        def filter2(root):
                root11 = Tk()
                root11.title('2nd Semester filter')
                #root.intro = Label(root10, text = "MOTTA GENERAL SECONDARY SCHOOL ROSTER", font = ("Arial", 10)) 
                #root.intro.grid(column = 0, row = 0, columnspan = 10)
                root.year = Label(root11, text = "YEAR...........................................", font = ("Arial", 10)) 
                root. year.grid(column = 0, row = 1,columnspan = 15)
                root. gread = Label(root11, text = "GR............................................", font = ("Arial", 10)) 
                root. gread.grid(column = 2, row = 1,columnspan = 15)
                root.section = Label(root11, text = "SECTION..................................", font = ("Arial", 10)) 
                root.section.grid(column = 3, row = 1,columnspan = 35)
                root. nam1 = Label(root11, text = "1st H.R.T Name.................................................................SIG................................................................", font = ("Arial", 10)) 
                root.nam1.grid(column = 1, row = 27, columnspan = 20)
                root.nam1 = Label(root11, text = "2nd H.R.T Name..........................................................SIG............DIRECTOR'S NAME:- EWUNETIE ADDIS.SIG.....................", font = ("Arial", 10)) 
                root. nam1.grid(column = 2, row = 28, columnspan = 20)
                 
                root.txt7 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt7.grid(column=6, row=4)
                root.txt7.insert(0,'AM')
                root.txt8 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt8.grid(column=7, row=4)
                root.txt8.insert(0,'EN')
                root.txt9 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt9.grid(column=8, row=4)
                root.txt9.insert(0,'MA')
                root.txt10 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt10.grid(column=9, row=4)
                root.txt10.insert(0,'PH')
                root.txt11 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt11.grid(column=10, row=4)
                root.txt11.insert(0,'CH')
                root.txt12 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt12.grid(column=11, row=4)
                root.txt12.insert(0,'BI')
                root.txt13 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt13.grid(column=12, row=4)
                root.txt13.insert(0,'GI')
                root.txt14 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt14.grid(column=13, row=4)
                root.txt14.insert(0,'HI')
                root.txt15 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt15.grid(column=14, row=4)
                root.txt15.insert(0,'CV')
                root.txt16 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt16.grid(column=15, row=4)
                root.txt16.insert(0,'HP')
                root.txt16 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt16.grid(column=16, row=4)
                root.txt16.insert(0,'IT')
                root.txt1 = Label(root11, text = ".",width=5)
                root.txt1.grid(column=0, row=4)  
                
                root.txt17 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt17.grid(column=5, row=5, ipady = 8)
                root.txt17.insert(0, '0-49')
                
                root.txt18 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt18.grid(column=5, row=6, ipady = 8)
                root.txt18.insert(0, 'M')
                
                root.txt19 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt19.grid(column=5, row=7, ipady = 8)
                root.txt19.insert(0, 'F')
                
                root.txt20 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt20.grid(column=5, row=8, ipady = 8)
                root.txt20.insert(0, '%')
                
                root.txt21 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt21.grid(column=5, row=9, ipady = 8)
                root.txt21.insert(0, '50-100')
                
                root.txt22 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt22.grid(column=5, row=10, ipady = 8)
                root.txt22.insert(0, 'M')
                
                root.txt23 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt23.grid(column=5, row=11, ipady = 8)
                root.txt23.insert(0, 'F')
                
                root.txt24 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt24.grid(column=5, row=12, ipady = 8)
                root.txt24.insert(0, '%')
                
                root.txt25 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt25.grid(column=5, row=13, ipady = 8)
                root.txt25.insert(0, '75-100')
                
                root.txt26 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt26.grid(column=5, row=14, ipady = 8)
                root.txt26.insert(0, 'M')
                
                root.txt27 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt27.grid(column=5, row=15, ipady = 8)
                root.txt27.insert(0, 'F')
                
                root.txt28 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt28.grid(column=5, row=16, ipady = 8)
                root.txt28.insert(0, '%')

                root.txt29 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt29.grid(column=5, row=17, ipady = 8)
                root.txt29.insert(0, '85-100')
                
                root.txt30 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt30.grid(column=5, row=18, ipady = 8)
                root.txt30.insert(0, 'M')
                
                root.txt31 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt31.grid(column=5, row=19, ipady = 8)
                root.txt31.insert(0, 'F')
                
                root.txt32 = ttk.Entry(root11,  width=8,font = ("Arial",11, "bold"))
                root.txt32.grid(column=5, row=20, ipady = 8)
                root.txt32.insert(0, '%')
                
                root.num1 = []
                for x in range(11):
                    for i in range(16):
                       
                       tt = ttk.Entry(root11,  width = 10,font = ("Arial",11,))
                       tt.grid(row = 5+i, column = 6+x,ipady = 8)
                       root.num1.append(tt)

                root.per = Label(root11, text = "Pleas Enter number of students", font = ("Arial, 11"))
                root.per.grid(column = 22, row = 5, columnspan = 6)
                
                root.per3 = ttk.Entry(root11, width = 7)
                root.per3.grid(column= 22, row = 6 )
                
                root.per2 = ttk. Button(root11, text= "oK", command = root.Add3)
                root.per2.grid(column= 22, row = 7)
                
                  

                                 
                
                root11.mainloop()


                
         
        def run(root):
            root.mainloop()
          
          
root= Tk()
root.title('Page -1')
app = App(root)
app.run()          
         
         
         
         
         
         
         
         
         
         
         
         
         
         