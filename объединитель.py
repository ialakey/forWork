from itertools import izip

with open('id_contacts.txt') as f1, open('email_id.txt') as f2, open('new.txt', 'w') as fout:
    for fst, snd in izip(f1, f2):
        fout.write('{0}:{1}\n'.format(fst.rstrip(), snd.rstrip()))