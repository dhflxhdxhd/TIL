package basic.graph.shortestpath;

class Node implements Comparable<Node>{
    int vertex; // 정점
    int weight; // 간선(가중치)

    public Node(int vertex, int weight) {
        this.vertex = vertex;
        this.weight = weight;
    }

    @Override
    public String toString() {
        return "(" + vertex + " , " + weight + ")";
    }

    // 가중치 기준 오름차순 정렬
    @Override
    public int compareTo(Node other) {
        return this.weight - other.weight;
    }
}
