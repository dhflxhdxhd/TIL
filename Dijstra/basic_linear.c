// 다익스트라 알고리즘 구현 - 순차 탐색
// "방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택"
// Implement Dijkstra Algorithm - Linear Search
// "Select the node with the shortest distance among unvisited nodes.

#include <stdio.h>
#include <stdbool.h>
#define size 8

int distance[size]; //최단 거리 노드 
bool visited[size]; // 방문한 노드

int a[size][size] = {
	{0,1,7,2,999,999,999},
	{1,0,999,999,2,4,999,999},
	{7,999,0,999,999,2,3,999},
	{2,999,999,0,999,999,5,999},
	{999,2,999,999,0,1,999,999},
	{999,4,2,999,1,0,999,6},
	{999,999,3,5,999,999,0,2},
	{999,999,999,999,999,6,2,0}
};

// 출발 정점에서 갈 수 있는 각 노드의 최소비용. -> 출발
// 가장 최소 거리를 가지는 정점
int get_smallest_node() {
	int min = 999;
	int index = 0;

	for (int i = 0; i < size; i++) {
		if (distance[i] < min && !visited[i]) {
			min = distance[i];
			index = i;
		}
	}
	return index;
}

void dijkstra(int start) {
	for (int i = 0; i < size; i++) {
		distance[i] = a[start - 1][i];
	}

	visited[start - 1] = true;
	for (int i = 0; i < size - 2; i++) {
		int now = get_smallest_node();
		printf("*%d", now);
		visited[now] = true;
		for (int j = 0; j < size; j++) {
			if (!visited[j]) {
				if (distance[now] + a[now][j] < distance[j]) {
					distance[j] = distance[now] + a[now][j];
				}
			}
		}
	}
}

int main() {
	dijkstra(1);
	for (int i = 0; i < size; i++) {
		printf("%d", distance[i]);
	}
	//Dijkstra(1, 7);
}
/*
순서
1. 출발 정점 선택 -> 입력
2. 출발 정점에서 갈 수 있는 각 노드의 최소비용. -> 출발
3. 2번에서 고른 것 중에 작은 노드부터 시작.

*/

// 입력 : 1,7 (출발정점, 도착정점)
// 출력 :
// 최단 경로 : 1->5->2->4->7
// 최단 비용 : 13

// kwonhoons2@gmail.com
