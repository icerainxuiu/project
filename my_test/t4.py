def generator_file_type_with_row_num(dict_data, change_dict, file_name, file_type, row_num):
    """
    按照给定的一个字典，文件名，文件类型，行数，生成一个指定的文件
    :param dict_data: 需要写入的原始模板字典
    :param change_dict: 在模板字典中需要改动的字典
    :param file_name: 文件名
    :param file_type: 文件类型
    :param row_num: 生成多少行
    :return:
    """
    gen_num = (i for i in range(row_num))
    data_keys = dict_data.keys()
    change_keys = change_dict.keys()

    for num in gen_num:
        len_dict_data = len(dict_data)
        for key in data_keys:
            len_dict_data -= 1
            if key not in change_keys:
                write_data(file_name, file_type, dict_data[key])
                write_seq(file_name, file_type, b=(len_dict_data > 0))
            else:
                write_data(file_name, file_type, dict_data[key]+"{}".format(num))
                write_seq(file_name, file_type, b=(len_dict_data > 0))


def write_data(file_name, file_type, data):
    """
    追加方式写入文件数据
    :param file_name:
    :param file_type:
    :param data:
    :return:
    """
    with open("./{}.{}".format(file_name, file_type), "a+", encoding="utf-8") as f:
        f.write(data)


def write_seq(file_name, file_type, sep=",", b=True):
    """
    写入文件的换行或者间隔符，默认间隔符为逗号","
    :param file_name:
    :param file_type:
    :param sep:分隔符
    :param b:
    :return:
    """
    if not b:
        write_data(file_name, file_type, data="\n")
    else:
        write_data(file_name, file_type, data=sep)


if __name__ == '__main__':
    json_data = {
        "project_name": "Plane",
        "gerrit_url": "http://192.168.11.88/gerrit1",
        "gerrit_port": "294181",
        "git_repo": "-",
        "branch": "archimedes",
        "branch_type": "public",
        "base_sha1": "-",
        "base_tag": "",
        "upstream_branch": "",
        "operation": "Add",
        "openrator": "dengge0914",
        "operation_time": "2019-06-21 16:27:17",
        "os_type": "",
        "os_version": "",
        "chip_type": "",
        "chip_version": "",
        "is_manifest_repo": "No",
        "description": "",
        "active": "Yes"
    }

    json_data1 = {"branch": "archimedes",
                  "branch_type": "public"}

    generator_file_type_with_row_num(json_data, json_data1, "data3", "txt", 5)
