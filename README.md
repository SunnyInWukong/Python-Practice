# Python Practice: Data Structures & Algorithms

## Overview
This repository contains my implementations of **fundamental data structures and algorithms in Python**, built from scratch to strengthen my understanding of:
- Algorithmic efficiency  
- Memory usage  
- Recursion and iteration  
- Clean, reusable code design  

Each implementation is written without relying on Python’s built-in collections (except where explicitly noted), to better simulate low-level behavior.

---

## Contents

### Trees
- **Binary Tree** (`BinaryTree`, `TreeNode`)  
  - Add nodes, find nodes, calculate size, height, depth  
  - Recursive node search and counting  
  - Future: traversals (inorder, preorder, postorder, level order), binary search trees, red/black trees, tries  

### Linked Lists
- **Single Linked List** (`SingleLinkedList`, `Node`)  
  - Append, print (iterative and recursive)  
  - Planned: remove, reverse, merge sort, quicksort, bubble sort  

- **Double Linked List** (`DoubleLinkedList`)  
  - Append, insert, remove by value/position  
  - Reverse list by pointer swapping  
  - Bubble sort implementation  
  - Planned: quicksort, mergesort, insertion sort, combine lists  

### Stacks & Queues
- **LinkedStack** – built using `DoubleLinkedList`  
  - `push`, `pop`, `peek`, `isEmpty`, `size`  
- **LinkedQueue** – also built on `DoubleLinkedList`  
  - FIFO operations with `push`, `pop`, `peek`, `isEmpty`, `size`  

### Search Algorithms
- **Binary Search** (recursive, for ordered arrays)  
- Planned: Linear Search, Jump Search, DFS/BFS for trees and graphs, Dijkstra’s, A*, Bellman-Ford  

---

## Goals
This project is ongoing and serves as practice for:
- Strengthening recursion skills  
- Implementing data structures without language shortcuts  
- Preparing for interviews and algorithm challenges  
- Building intuition for how higher-level ML/AI and system algorithms work under the hood  

---

## Next Steps
- Add traversal algorithms for binary trees (DFS, BFS)  
- Implement full set of sorting algorithms on linked lists  
- Add graph representation (adjacency list & adjacency matrix)  
- Implement pathfinding algorithms (Dijkstra’s, A*, Bellman-Ford)  

---

## Usage
Clone the repo and run the files directly for testing:

```bash
git clone https://github.com/SunniyInWukong/Python-Practice.git
cd Python-Practice
python3 BinaryTree.py

