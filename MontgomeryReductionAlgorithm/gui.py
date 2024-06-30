import tkinter as tk
from tkinter import messagebox

from MontgomeryReductionAlgorithm.mmr import MMR
from MontgomeryReductionAlgorithm.srsa import RSA



class MMRGui(tk.Tk):


    def __init__(self):
        super().__init__()
        self.title("Montgomery Reduction Algorithm")
        self.create_widgets()
        self.create_menu()


    def create_menu(self):
        menu_bar = tk.Menu(self)
        
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Clear", command=self.clear)
        file_menu.add_command(label="Close", command=self.close)
        menu_bar.add_cascade(label="Menu", menu=file_menu)
        
        convert_menu = tk.Menu(menu_bar, tearoff=0)
        convert_menu.add_command(label="To Hexadecimal", command=self.convert_to_hexadecimal)
        convert_menu.add_command(label="To Decimal", command=self.convert_to_decimal)
        menu_bar.add_cascade(label="Convert", menu=convert_menu)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Version", command=self.show_version_info)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        
        self.config(menu=menu_bar)
    

    def show_version_info(self):
        messagebox.showinfo("Version", "Version: 0.0.4-beta\nLicense: MIT\nAuthor: Andreas W. Weber")


    def create_widgets(self):

        frame_primes = tk.LabelFrame(self, text="Prime Numbers", padx=10, pady=10)
        frame_primes.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(frame_primes, text="Max q:").grid(row=0, column=0)
        self.entry_max_q = tk.Entry(frame_primes)
        self.entry_max_q.grid(row=0, column=1)
        self.entry_max_q.insert(0, str(100))

        tk.Label(frame_primes, text="Primes:").grid(row=1, column=0)
        self.text_primes = tk.Text(frame_primes, height=6, width=20, state="disabled")
        self.text_primes.grid(row=1, column=1)

        tk.Button(frame_primes, text="Find Primes", command=self.find_primes).grid(row=2, columnspan=4)

        frame_rsa = tk.LabelFrame(self, text="RSA", padx=10, pady=10)
        frame_rsa.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(frame_rsa, text="Prime Number p:").grid(row=3, column=0)
        self.entry_p = tk.Entry(frame_rsa)
        self.entry_p.grid(row=3, column=1)
        
        tk.Label(frame_rsa, text="Prime Number q:").grid(row=4, column=0)
        self.entry_q = tk.Entry(frame_rsa)
        self.entry_q.grid(row=4, column=1)
                
        tk.Label(frame_rsa, text="Modulus n:").grid(row=5, column=0)
        self.entry_n = tk.Entry(frame_rsa, state="readonly")
        self.entry_n.grid(row=5, column=1)
        
        tk.Label(frame_rsa, text="Euler's Totient φ(n):").grid(row=6, column=0)
        self.entry_tot = tk.Entry(frame_rsa, state="readonly")
        self.entry_tot.grid(row=6, column=1)
        
        tk.Label(frame_rsa, text="Public Key e:").grid(row=7, column=0)
        self.entry_e1 = tk.Entry(frame_rsa, state="readonly")
        self.entry_e1.grid(row=7, column=1)
        
        tk.Label(frame_rsa, text="Private Key d:").grid(row=8, column=0)
        self.entry_d = tk.Entry(frame_rsa, state="readonly")
        self.entry_d.grid(row=8, column=1)

        tk.Button(frame_rsa, text="Calculate RSA Values", command=self.calculate_rsa).grid(row=9, columnspan=4)

        frame_mme = tk.LabelFrame(self, text="MME", padx=10, pady=10)
        frame_mme.grid(row=1, column=0, padx=10, pady=10)

        tk.Label(frame_mme, text="Message m:").grid(row=10, column=0)
        self.entry_m = tk.Entry(frame_mme)
        self.entry_m.grid(row=10, column=1)
        
        tk.Label(frame_mme, text="Public Key e:").grid(row=11, column=0)
        self.entry_e2 = tk.Entry(frame_mme)
        self.entry_e2.grid(row=11, column=1)

        tk.Label(frame_mme, text="Modulus n:").grid(row=12, column=0)
        self.entry_n1 = tk.Entry(frame_mme)
        self.entry_n1.grid(row=12, column=1)
        
        tk.Label(frame_mme, text="k=2^{2N}:").grid(row=13, column=0)
        self.entry_k = tk.Entry(frame_mme)
        self.entry_k.grid(row=13, column=1)

        tk.Label(frame_mme, text="MME:").grid(row=14, column=0)
        self.entry_mme = tk.Entry(frame_mme, state="readonly")
        self.entry_mme.grid(row=14, column=1)

        tk.Button(frame_mme, text="Calculate MME", command=self.calculate_mme).grid(row=15, columnspan=4)

        frame_mmm = tk.LabelFrame(self, text="MMM", padx=10, pady=10)
        frame_mmm.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(frame_mmm, text="Natural Number a:").grid(row=16, column=0)
        self.entry_a = tk.Entry(frame_mmm)
        self.entry_a.grid(row=16, column=1)
        
        tk.Label(frame_mmm, text="Natural Number b:").grid(row=17, column=0)
        self.entry_b = tk.Entry(frame_mmm)
        self.entry_b.grid(row=17, column=1)

        tk.Label(frame_mmm, text="Modulus n:").grid(row=18, column=0)
        self.entry_n2 = tk.Entry(frame_mmm)
        self.entry_n2.grid(row=18, column=1)

        tk.Label(frame_mmm, text="MMM:").grid(row=19, column=0)
        self.entry_mmm = tk.Entry(frame_mmm, state="readonly")
        self.entry_mmm.grid(row=19, column=1)

        tk.Button(frame_mmm, text="Calculate MMM", command=self.calculate_mmm).grid(row=20, columnspan=4)

        frame_encryption = tk.LabelFrame(self, text="Encryption", padx=10, pady=10)
        frame_encryption.grid(row=2, column=0, padx=10, pady=10)

        tk.Label(frame_encryption, text="Message m:").grid(row=21, column=0)
        self.entry_m1 = tk.Entry(frame_encryption)
        self.entry_m1.grid(row=21, column=1)

        tk.Label(frame_encryption, text="Public Key e:").grid(row=22, column=0)
        self.entry_e3 = tk.Entry(frame_encryption)
        self.entry_e3.grid(row=22, column=1)

        tk.Label(frame_encryption, text="Modulus n:").grid(row=23, column=0)
        self.entry_n3 = tk.Entry(frame_encryption)
        self.entry_n3.grid(row=23, column=1)

        tk.Label(frame_encryption, text="Ciphertext c:").grid(row=24, column=0)
        self.entry_c1 = tk.Entry(frame_encryption, state="readonly")
        self.entry_c1.grid(row=24, column=1)

        tk.Button(frame_encryption, text="Encrypt", command=self.calculate_encryption).grid(row=25, columnspan=4)

        frame_decryption = tk.LabelFrame(self, text="Decryption", padx=10, pady=10)
        frame_decryption.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(frame_decryption, text="Ciphertext c:").grid(row=26, column=0)
        self.entry_c2 = tk.Entry(frame_decryption)
        self.entry_c2.grid(row=26, column=1)

        tk.Label(frame_decryption, text="Private Key d:").grid(row=27, column=0)
        self.entry_d1 = tk.Entry(frame_decryption)
        self.entry_d1.grid(row=27, column=1)

        tk.Label(frame_decryption, text="Modulus n:").grid(row=28, column=0)
        self.entry_n4 = tk.Entry(frame_decryption)
        self.entry_n4.grid(row=28, column=1)

        tk.Label(frame_decryption, text="Message m:").grid(row=29, column=0)
        self.entry_m2 = tk.Entry(frame_decryption, state="readonly")
        self.entry_m2.grid(row=29, column=1)

        tk.Button(frame_decryption, text="Decrypt", command=self.calculate_decryption).grid(row=30, columnspan=4)

        frame_general = tk.LabelFrame(self, text="General", padx=10, pady=10)
        frame_general.grid(row=3, column=1, padx=10, pady=10)

        tk.Button(frame_general, text="Clear", command=self.clear).grid(row=31, column=0)
        tk.Button(frame_general, text="Close", command=self.close).grid(row=31, column=1)

        frame_convert = tk.LabelFrame(self, text="Convert", padx=10, pady=10)
        frame_convert.grid(row=3, column=0, padx=10, pady=10)

        tk.Button(frame_convert, text="To Hexadecimal", command=self.convert_to_hexadecimal).grid(row=31, column=0)
        tk.Button(frame_convert, text="To Decimal", command=self.convert_to_decimal).grid(row=31, column=1)


    def set_entry_value(self, entry, value, state='readonly'):
        entry.config(state='normal')
        entry.delete(0, tk.END)
        entry.insert(0, value)
        entry.config(state=state)


    def set_text_value(self, text, value, state='disabled'):
        text.config(state='normal')
        text.delete('1.0', 'end')
        text.insert('1.0', value)
        text.config(state=state)


    def close(self):
        self.destroy()


    def clear(self):
        self.entry_max_q.delete(0, tk.END)
        self.entry_max_q.insert(0, str(100))
        self.set_text_value(self.text_primes, "")

        self.entry_p.delete(0, tk.END)
        self.entry_q.delete(0, tk.END)
        self.set_entry_value(self.entry_n, "")
        self.set_entry_value(self.entry_tot, "")
        self.set_entry_value(self.entry_e1, "")
        self.set_entry_value(self.entry_d, "")

        self.entry_m.delete(0, tk.END)
        self.entry_e2.delete(0, tk.END)
        self.entry_n1.delete(0, tk.END)
        self.entry_k.delete(0, tk.END)
        self.set_entry_value(self.entry_mme, "")

        self.entry_a.delete(0, tk.END) 
        self.entry_b.delete(0, tk.END)
        self.entry_n2.delete(0, tk.END)
        self.set_entry_value(self.entry_mmm, "")

        self.entry_m1.delete(0, tk.END) 
        self.entry_e3.delete(0, tk.END)
        self.entry_n3.delete(0, tk.END)
        self.set_entry_value(self.entry_c1, "")

        self.entry_c2.delete(0, tk.END) 
        self.entry_d1.delete(0, tk.END)
        self.entry_n4.delete(0, tk.END)
        self.set_entry_value(self.entry_m2, "")


    def find_primes(self):
        try:
            q_max = int(self.entry_max_q.get(), 0)

            primes = RSA.sieve_of_eratosthenes(q_max=q_max)
            primes = [str(p) for p in primes]
            self.set_text_value(self.text_primes, str(",".join(primes)))
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers.")


    def calculate_rsa(self):
        try:
            p = int(self.entry_p.get(), 0)
            q = int(self.entry_q.get(), 0)

            n = RSA.n(p, q)
            self.set_entry_value(self.entry_n, str(n))

            tot = RSA.tot(p, q)
            self.set_entry_value(self.entry_tot, str(tot))

            e = RSA.e(tot)
            self.set_entry_value(self.entry_e1, str(e))

            d = RSA.d(e, tot)
            self.set_entry_value(self.entry_d, str(d))
        except ValueError:
            self.clear()
            messagebox.showerror("Input Error", "Please enter valid integers.")
        except Exception as e:
            self.clear()
            messagebox.showerror("Error", e)


    def calculate_mme(self):
        try:
            m = int(self.entry_m.get(), 0)
            e = int(self.entry_e2.get(), 0)
            n = int(self.entry_n1.get(), 0)
            k = int(self.entry_k.get(), 0)

            mme = MMR.mme(m, e, n, k)
            self.set_entry_value(self.entry_mme, str(mme))
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers.")


    def calculate_mmm(self):
        try:
            a = int(self.entry_a.get(), 0)
            b = int(self.entry_b.get(), 0)
            n = int(self.entry_n2.get(), 0)

            mmm = MMR.mmm(a, b, n)
            self.set_entry_value(self.entry_mmm, str(mmm))
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers.")


    def calculate_encryption(self):
        try:
            m = int(self.entry_m1.get(), 0)
            e = int(self.entry_e3.get(), 0)
            n = int(self.entry_n3.get(), 0)

            c = RSA.encrypt(m, e, n)
            self.set_entry_value(self.entry_c1, str(c))
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers.")
        except Exception as e:
            self.clear()
            messagebox.showerror("Error", e)


    def calculate_decryption(self):
        try:
            c = int(self.entry_c2.get(), 0)
            d = int(self.entry_d1.get(), 0)
            n = int(self.entry_n4.get(), 0)

            m = RSA.decrypt(c, d, n)
            self.set_entry_value(self.entry_m2, str(m))
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers.")
        except Exception as e:
            self.clear()
            messagebox.showerror("Error", e)


    def text_convert_to(self, text, numerative='decimal'):
        try:
            txt = text.get('1.0', 'end').strip()
            if txt:
                txt = txt.strip().split(',')
                txt = [int(t.strip(), 0) for t in txt]
                if numerative == 'hexadecimal':
                    txt = [str(hex(t)) for t in txt]
                txt = ",".join([str(t) for t in txt])
                self.set_text_value(text, txt)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers.")
        except Exception as e:
            self.clear()
            messagebox.showerror("Error", e)


    def entry_convert_to(self, entry, numerative='decimal', state='normal'):
        try:
            txt = entry.get()
            if txt:
                txt = int(txt, 0)
                if numerative == 'hexadecimal':
                    txt = hex(txt)
                txt = str(txt)
                self.set_entry_value(entry, txt, state=state)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers.")
        except Exception as e:
            self.clear()
            messagebox.showerror("Error", e)



    def convert_to(self, numerative='decimal'):
        try:
            self.text_convert_to(self.text_primes, numerative)

            self.entry_convert_to(self.entry_p, numerative=numerative)
            self.entry_convert_to(self.entry_q, numerative=numerative)

            self.entry_convert_to(self.entry_n, numerative=numerative, state='readonly')
            self.entry_convert_to(self.entry_tot, numerative=numerative, state='readonly')
            self.entry_convert_to(self.entry_e1, numerative=numerative, state='readonly')
            self.entry_convert_to(self.entry_d, numerative=numerative, state='readonly')

            self.entry_convert_to(self.entry_m, numerative=numerative)
            self.entry_convert_to(self.entry_e2, numerative=numerative)
            self.entry_convert_to(self.entry_n1, numerative=numerative)
            self.entry_convert_to(self.entry_k, numerative=numerative)
            self.entry_convert_to(self.entry_mme, numerative=numerative, state='readonly')

            self.entry_convert_to(self.entry_a, numerative=numerative)
            self.entry_convert_to(self.entry_b, numerative=numerative)
            self.entry_convert_to(self.entry_n2, numerative=numerative)
            self.entry_convert_to(self.entry_mmm, numerative=numerative, state='readonly')

            self.entry_convert_to(self.entry_m1, numerative=numerative)
            self.entry_convert_to(self.entry_e3, numerative=numerative)
            self.entry_convert_to(self.entry_n3, numerative=numerative)
            self.entry_convert_to(self.entry_c1, numerative=numerative, state='readonly')

            self.entry_convert_to(self.entry_c2, numerative=numerative)
            self.entry_convert_to(self.entry_d1, numerative=numerative)
            self.entry_convert_to(self.entry_n4, numerative=numerative)
            self.entry_convert_to(self.entry_m2, numerative=numerative, state='readonly')

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers.")
        except Exception as e:
            self.clear()
            messagebox.showerror("Error", e)


    def convert_to_hexadecimal(self):
        self.convert_to(numerative='hexadecimal')

    
    def convert_to_decimal(self):
        self.convert_to(numerative='decimal')


def main():
    app = MMRGui()
    app.mainloop() 


if __name__ == "__main__":
    main()