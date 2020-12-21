package com.company;

import com.company.algorithm.BinaryTreeAlgorithms;
import com.company.classes.BinaryTree;
import com.company.classes.Node;
import com.company.creator.BinaryTreeCreator;

public class Main {

    static final int COUNT_ELEMENTS = 16;
    static final int START = 0;
    static final int END = 120;
    static final int KEY = 16;

    public static void main(String[] args) {
        BinaryTreeCreator binaryTreeCreator = new BinaryTreeCreator();
        BinaryTree binaryTree = binaryTreeCreator.createBinaryTree(START, END, COUNT_ELEMENTS);
        System.out.println(binaryTree.toString());

        BinaryTreeAlgorithms binaryTreeAlgorithm = new BinaryTreeAlgorithms();
        binaryTreeAlgorithm.symmetricTraversal(binaryTree.getRoot());

        long startTime = System.nanoTime();
        Node key = binaryTreeAlgorithm.search(binaryTree.getRoot(), KEY);
        long endTime = System.nanoTime();
        long leadTime = endTime - startTime;
        System.out.println("\nKey nearby from above: " + key.getValue());
        System.out.println("Lead time = " + leadTime);


    }
}