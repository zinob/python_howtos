#!/usr/bin/python

## """
## How do i parallelize a retriever function and a sender/saver function when they
## 1: require mpthreads
## 2: The dataammount is significant enough that I don't want the receiver to get to far ahead of the sender.
## """
## This code uses a semaphore to bound the amount of in-flight data.
## The general rule of thumb is that you should use twice the number of threads that you have CPUs,
## so this one uses one pool for senders and one pool for receivers, each with equal workers as there are CPUs in the system.
## The semaphore size is set to the twice the number of possible in-flight sending requests in order to avoid thread starvation
## (if it is less than cpu*chunk it will stall, if its less than twice that performance might suffer)

import multiprocessing
from multiprocessing import Pool
import time
try:
    from tqdm import tqdm
except:
    tqdm=lambda x:x:
import random

def ini(y):
    global semaphore
    semaphore=y
    
def receive(i):
    semaphore.acquire()
    time.sleep(1+random.randrange(-4,4)/10)
    return i+1

def send(x):
    time.sleep(2)
    semaphore.release()
    return(f"sent:{x}")


ITERS=99
CHUNK=4
CPUs=multiprocessing.cpu_count()

m = multiprocessing.Manager()
s = m.BoundedSemaphore(CHUNK*CPUs*2)
t=time.time()
with Pool(CPUs,initializer=ini, initargs=[s] ) as receiver_p:
    with Pool(CPUs,initializer=ini, initargs=[s]) as sender_p:
        indata = range(ITERS)
        received=receiver_p.imap_unordered(receive, indata,chunksize=CHUNK)
        sent=sender_p.imap_unordered(send, tqdm(received, desc="received", total=ITERS,miniters=1),chunksize=CHUNK)
        for i in tqdm(sent,desc="sent",total=ITERS,miniters=1):
            pass

        time.sleep(1)
        print()
        print(time.time()-t)
print(time.time()-t)
