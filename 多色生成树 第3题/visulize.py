import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(edges, mst_edges):
    """
    可视化原始图和最小生成树，左右对比，确保两个图在相同布局下显示
    :param edges: 图的边列表，每条边格式为 (u, v, color)，
                  其中 u 和 v 是节点，color 是边的颜色（'red' 或 'blue'）
    :param mst_edges: 最小生成树的边列表，每条边格式为 (u, v, color)
    """
    # 检查输入是否为空
    if not edges or not mst_edges:
        raise ValueError("边列表不能为空")

    # 创建图
    G = nx.Graph()

    # 检查每条边的数据格式是否正确
    for edge in edges:
        if len(edge) != 3:
            raise ValueError(f"边数据格式错误：{edge}，每条边应包含三个元素 (u, v, color)")
        
        u, v, color = edge
        if not isinstance(u, int) or not isinstance(v, int):
            raise ValueError(f"边的节点应为整数，错误的节点数据：{u}, {v}")
        
        if color not in ['red', 'blue']:
            raise ValueError(f"边的颜色应为 'red' 或 'blue'，错误的颜色：{color}")
        
        # 添加边到图中
        G.add_edge(u, v, color=color)

    # 获取图的布局，设置随机种子为12，使图的样式一致
    pos = nx.spring_layout(G, seed=12)

    # 创建一个包含两个子图的画布
    fig, axs = plt.subplots(1, 2, figsize=(16, 8))

    # 绘制原始图（左图）
    edge_colors = [G[u][v]['color'] for u, v in G.edges()]
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue', ax=axs[0])  # 绘制节点
    nx.draw_networkx_labels(G, pos, font_size=15, ax=axs[0])  # 绘制标签
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2, alpha=0.6, ax=axs[0])  # 绘制边
    axs[0].set_title("Original Graph")
    axs[0].axis('off')  # 关闭坐标轴

    # 绘制最小生成树（右图）
    mst_edge_colors = ['blue' if color == 'blue' else 'red' for u, v, color in mst_edges]
    
    # 绘制最小生成树
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue', ax=axs[1])  # 绘制节点
    nx.draw_networkx_labels(G, pos, font_size=15, ax=axs[1])  # 绘制标签
    nx.draw_networkx_edges(G, pos, edgelist=[(u, v) for u, v, _ in mst_edges], 
                           edge_color=mst_edge_colors, width=2, alpha=0.6, ax=axs[1])  # 绘制边
    axs[1].set_title("Spanning Tree")
    axs[1].axis('off')  # 关闭坐标轴

    # 显示两个图
    plt.show()
