n = (x for x in range(1, 10001))
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

for i in n:
    with open("./data.csv", "a+", encoding="utf-8") as f:

        f.write("{},{},{}{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(json_data["project_name"],
                                                                                json_data["gerrit_url"],
                                                                                json_data["gerrit_port"],
                                                                                i,
                                                                                json_data["git_repo"],
                                                                                json_data["branch"],
                                                                                json_data["branch_type"],
                                                                                json_data["base_sha1"],
                                                                                json_data["base_tag"],
                                                                                json_data["upstream_branch"],
                                                                                json_data["operation"],
                                                                                json_data["openrator"],
                                                                                json_data["operation_time"],
                                                                                json_data["os_type"],
                                                                                json_data["os_version"],
                                                                                json_data["chip_type"],
                                                                                json_data["is_manifest_repo"],
                                                                                json_data["description"],
                                                                                json_data["active"]))
