# crib_dragging
This is the programming assignment from COMP 3632.

ctext0 and ctext1 are the encrypted ciphertexts given.
ptext0 and ptext1 are the plaintexts decrypted by crib dragging algorithm.

crib dragging algorithm: 

C1⊕C2 = (P1⊕K)⊕(P2⊕K) = (P1⊕P2)⊕(K⊕K) = P1⊕P2
Guess a word (W) and XOR W with C1⊕C2. If the result is readable, the guess may be correct. Continue to guess until the whole passage is readable.

