import re

journal_map = {
    "IEEE Internet of Things Journal": r"\textit{IEEE Internet Things J.}",
    "IEEE Transactions on Communications": r"\textit{IEEE Trans. Commun.}",
    "IEEE Transactions on Wireless Communications": r"\textit{IEEE Trans. Wireless Commun.}",
    "IEEE Transactions on Signal Processing": r"\textit{IEEE Trans. Signal Process.}",
    "IEEE Communications Magazine": r"\textit{IEEE Commun. Mag.}",
    "IEEE Journal on Selected Areas in Communications": r"\textit{IEEE J. Sel. Areas Commun.}"
}

def ieee_to_latex(ref: str) -> str:
    # 去掉 doi
    ref = re.sub(r"doi:.*", "", ref)

    # 日期规范化：只保留 Jan. 2025
    ref = re.sub(r"\d{1,2}\s*Jan\.?\.?\s*\d{0,2},?\s*", "Jan. ", ref)

    # 作者部分
    parts = ref.split(",", 4)
    authors = ",".join(parts[:4])
    rest = parts[4] if len(parts) > 4 else ""

    author_list = re.split(r",| and ", authors)
    author_list = [a.strip() for a in author_list if a.strip()]

    if len(author_list) > 3:
        author_str = ", ".join(author_list[:3]) + r" \textit{et al.}"
    else:
        author_str = ", ".join(author_list)

    # 替换引号
    rest = rest.replace('"', "``", 1).replace('"', "''", 1)

    # 去掉 "in "
    rest = re.sub(r"\bin\s+", "", rest)

    # 替换期刊名为缩写
    for full, abbr in journal_map.items():
        if full in rest:
            rest = rest.replace(full, abbr)

    # 末尾确保句号
    rest = rest.strip().rstrip(",") + "."

    return f"{author_str},{rest}"

if __name__ == "__main__":
    print("请输入 IEEE 引文：")
    s = input().strip()
    print("\n转换结果：")
    print(ieee_to_latex(s))
