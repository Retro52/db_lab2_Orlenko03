import matplotlib.pyplot as plt
import config
import query
import matplotlib
import sys

matplotlib.use('TkAgg')


def get_color(_hash: int):
    _norm = abs(_hash) * (256 ** 3) / (2 ** (sys.hash_info.width - 1))
    return f'#{str(hex(round(_norm))).replace("0x", "").upper()}FF'


def create_visualisations(_fname=None, _format='svg'):
    _q1_res = query.get_query_result(query.query_1)
    _q2_res = query.get_query_result(query.query_2)
    _q3_res = query.get_query_result(query.query_3)

    _figure, (_bar_ax, _pie_ax, _graph_ax) = plt.subplots(1, 3)

    _bar_ax.bar(range(len(_q1_res)), height=[_item[1] for _item in _q1_res])
    _bar_ax.set_title('Number of AMD CPUs released by year')
    _bar_ax.set_xlabel('Year')
    _bar_ax.set_ylabel('Number of releases')
    _bar_ax.set_xticks(range(len(_q1_res)))
    _bar_ax.set_xticklabels([str(_item[0]) for _item in _q1_res], rotation=45)

    _pie_ax.pie([_item[1] for _item in _q2_res], labels=[str(_item[0]) for _item in _q2_res],
                autopct=lambda p: '{:.1f}%; {:,.0f}'.format(p, p * sum([_item[1] for _item in _q2_res]) / 100),
                textprops={'fontsize': 5},
                colors=[get_color(hash(_item)) for _item in _q2_res],
                radius=1.15)
    _pie_ax.set_title('Total threads count distribution among AMD CPUs:')

    _graph_ax.plot([int(_item[0]) for _item in _q3_res], [int(_item[1]) for _item in _q3_res], marker='^')
    _graph_ax.set_xlabel('Year')
    _graph_ax.set_ylabel('Lithography size, nm')
    _graph_ax.set_title('Minimal lithography size available')

    _mng = plt.get_current_fig_manager()
    _mng.resize(5000, 2000)
    plt.subplots_adjust(left=0.1, bottom=0.15, right=0.975, top=0.9, wspace=0.4, hspace=0.4)

    if _fname is not None:
        plt.tight_layout()
        plt.gcf().set_size_inches(15, 5)
        plt.savefig(_fname + f".{_format}", dpi=500, format=_format)

    plt.show()
