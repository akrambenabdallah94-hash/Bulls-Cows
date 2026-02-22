import partieBC
import unittest
import random 

class TestPartiBC(unittest.TestCase):
    def combinaison_secrete_test(self, n):
        for _ in range (n):
            test = partieBC.combinaison_secrete()
            #verifier si une fonction est une liste
            self.assertIsInstance(test, list)
            #verifier qu'elle contient 4 éléments
            self.assertEqual(len(test), 4)

            #verifier que chaque éléments est un entier entre 0 et 9
            for valeur in test:
                self.assertIsInstance(valeur, int)  

                self.assertGreaterEqual(valeur, 0)
                self.assertLessEqual(valeur, 9)

    # c'est une methode qui appel la methode combinaison_secrete_test(self, n)
    def test_combinaison_secrete(self):
        self.combinaison_secrete_test(100)

    def test_histo(self):
        self.assertEqual(partieBC.histo([3, 6, 3, 1]), [0, 1, 0, 2, 0, 0, 1, 0, 0, 0])

    def test_histo_m_et_n(self):
        for _ in range(1000):
            m = random.randint(0, 9)
            n = random.randint(0, 9)

            L = [m, n, n, m]
            resultat = partieBC.histo(L)

            non_nuls = sum(1 for x in resultat if x != 0)
            
            if m == n:
                self.assertEqual(non_nuls, 1)
                self.assertEqual(resultat[m], 4)
            else: 
                self.assertEqual(non_nuls, 2)
                self.assertEqual(resultat[m], 2)
                self.assertEqual(resultat[n], 2)


    def test_nombre_communs(self):
        self.assertEqual(partieBC.nombre_communs([1, 2, 3, 4],[5, 6, 7, 8]), 0)
        self.assertEqual(partieBC.nombre_communs([1, 2, 3, 4],[4, 5, 6, 7]), 1)
        self.assertEqual(partieBC.nombre_communs([1, 2, 3, 4],[3, 4, 5, 6]), 2)
        self.assertEqual(partieBC.nombre_communs([1, 2, 3, 4],[2, 3, 4, 5]), 3)
        self.assertEqual(partieBC.nombre_communs([1, 2, 3, 4],[1, 2, 3, 4]), 4)

    def test_nombre_commus_m_et_n(self):
        for _ in range(1000):

            m = random.randint(0, 9)
            n = random.randint(0, 9)

            a = partieBC.nombre_communs([m, 1, 1, 1], [n, 2, 2, 2])
            b = partieBC.nombre_communs([1, m, 1, 1], [2, n, 2, 2])
            c = partieBC.nombre_communs([1, 1 ,1, m], [2, 2, 2, n])
            d = partieBC.nombre_communs([m, m, m, m], [n, n, n ,n])
            
            if m == n:
                self.assertEqual(a, 1)
                self.assertEqual(b, 1)
                self.assertEqual(c, 1)
                self.assertEqual(d, 4)
            elif m == 2 and n == 1:
                self.assertEqual(a, 2)
                self.assertEqual(b, 2)
                self.assertEqual(c, 2)
                self.assertEqual(d, 0)
            elif m == 2 and n != 1:
                self.assertEqual(a, 1)
                self.assertEqual(b, 1)
                self.assertEqual(c, 1)
                self.assertEqual(d, 0)
            elif m != 2 and n == 1:
                self.assertEqual(a, 1)
                self.assertEqual(b, 1)
                self.assertEqual(c, 1)
                self.assertEqual(d, 0)
            else:
                self.assertEqual(a, 0)
                self.assertEqual(b, 0)
                self.assertEqual(c, 0)
                self.assertEqual(d, 0)


    def test_nombre_bulls_cows(self): 
        from collections import Counter
        for _ in range(10):
            config1 = [random.randint(0, 9) for _ in range(4)]
            config2 = [random.randint(0, 9) for _ in range(4)] 
            taille = len(config1)

            a = partieBC.nombre_bulls_cows(config1, config2)
            
            count = 0
            for chiffre in range(taille):
                if config1[chiffre] == config2[chiffre]:
                    count += 1

            x = Counter(config1)
            y = Counter(config2)

            countc = 0
            for chiffre in x:
                if chiffre in y:
                    countc += min(x[chiffre], y[chiffre])

            resultat = countc - count     

            if resultat < 0:
                print(resultat)

            if count == 1 : 
                self.assertEqual(a, (1, resultat))
            elif count == 2:
                self.assertEqual(a, (2, resultat))
            elif count == 3 :
                self.assertEqual(a, (3, resultat))
            elif count == 4 :
                self.assertEqual(a, (4, 0))
                              
        
if __name__ == "__main__":
    unittest.main()

    pass