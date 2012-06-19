from gi.repository import Gtk
import shelve
   
class Window:

   def check(self,widget,data,parent,contact,phone_no):
       if data == 1:
           contacts = shelve.open('database.dat')
           contacts[contact] = phone_no
           contacts.close()   
       parent.destroy() 

   def Dialog(self,contact,phone_no):
       window = Gtk.Window()
       window.set_size_request(100,100)
       button1 = Gtk.Button(label = 'YES')
       label = Gtk.Label('%s already exists.Do you want to replace' % (contact))
       button2 = Gtk.Button(label = 'NO') 
       tabel = Gtk.Table(5,5,True)    
       tabel.attach(label,1,4,1,2)
       tabel.attach(button1,1,2,3,4)
       tabel.attach(button2,3,4,3,4)
       window.add(tabel)
       button1.connect('clicked',self.check,1,window,contact,phone_no)        
       button2.connect('clicked',self.check,2,window,contact,phone_no)
       window.show_all()



    
   def __init__(self):
       self.window = Gtk.Window(title = 'Store Contacts')
       self.window.connect('delete-event',Gtk.main_quit)
       self.window.set_size_request(300,300)
       self.table = Gtk.Table(10,10,True)
       self.entry1 = Gtk.Entry()
       
       self.entry1.set_text('Enter name')
       self.entry1.connect('changed',self.search)
       self.entry2 = Gtk.Entry()
       self.entry2.set_text('Enter phone number')
       self.button3 = Gtk.Button(label = 'Store Contact')
       self.button3.connect('clicked',self.store)
       self.button4 = Gtk.Button(label = 'Search Contact')
       self.table.attach(self.entry1,2,8,2,3)
       self.table.attach(self.entry2,2,8,4,5)
       self.table.attach(self.button3,2,4,6,8)
       self.table.attach(self.button4,6,8,6,8)
       self.window.add(self.table)       
       self.window.show_all()

   
        
   def store(self,widget):
       name = self.entry1.get_text()
       name = ''.join(list(name.strip().lower()))
       phone_no = self.entry2.get_text()
       contacts = shelve.open('database.dat')               
       for contact in contacts:
           if contact == name:               
               self.Dialog(contact,phone_no)               
               return
       contacts[name] = phone_no                  
       contacts.close()


   def search(self,widget):
       text = (widget.get_text()).lower()
       contacts = shelve.open('database.dat')
       for contact in contacts:
           if contact == text:
               self.entry2.set_text(contacts[contact])
               contacts.close()  
               return
       self.entry2.set_text('No search found')
       contacts.close()
       return


        
       

def main():
   Window()
   Gtk.main()


if __name__ == '__main__':
    main()
