from __future__ import annotations
from typing import Optional
from . import base_api


class USBCopy(base_api.BaseApi):
    """ """

    def usb_copy_info(self, task_id: int) -> dict[str, object] | str:
        """Retrieve task information

            Parameters
            ----------
            id: int
                Task ID to retrieve info for

            Returns
            -------
            dict[str, object]
                Parsed response JSON into `dict`

            Example return:
            --------------
            ```python
            {
                "data" : {
                    "task" : {
                        "conflict_policy" : "rename",
                        "copy_file_path" : "",
                        "copy_strategy" : "versioning",
                        "default_device_port" : "NA",
                        "destination_path" : "[USB]",
                        "eject_when_task_done" : True,
                        "enable_rotation" : False,
                        "error_code" : 0,
                        "id" : 2,
                        "is_default_task" : False,
                        "is_ds_mounted" : False,
                        "is_task_runnable" : False,
                        "is_usb_mounted" : False,
                        "latest_finish_time" : 1738341351,
                        "max_version_count" : 256,
                        "name" : "asdf",
                        "next_run_time" : "N/A",
                        "not_keep_dir_structure" : False,
                        "remove_src_file" : False,
                        "rename_photo_video" : False,
                        "rotation_policy" : "oldest_version",
                        "run_when_plug_in" : False,
                        "schedule_id" : 13,
                        "smart_create_date_dir" : False,
                        "source_path" : "/music",
                        "status" : "unmounted",
                        "type" : "export_general"
                    }
                },
                "success" : True
            }
            ```

        """
        api_name = 'SYNO.USBCopy'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get', 'id': id}

        return self.request_data(api_name, api_path, req_param)


    def toggle_usb_copy(self, task_id: int, enable: bool = True) -> dict[str, object] | str:
        """Enable or disable USB Copy task

            Parameters
            ----------
            enable : bool, default=True
                Whether to enable (`True`) or disable (`False`) USB Copy.
            task_id : int
                Task ID to apply the setting to.

            Returns
            -------
            dict[str, object]
                Parsed response JSON into `dict`

            Example return:
            --------------
            ```python
            {
                "success": True
            }
            ```

        """
        api_name = 'SYNO.USBCopy'
        info = self.gen_list[api_name]
        api_path = info['path']

        if enable:
            enable = 'enable'
        elif not enable:
            enable = 'disable'
        else:
            return 'enable must be True or False'

        req_param = {'version': info['maxVersion'], 'method': enable, 'id': task_id}

        return self.request_data(api_name, api_path, req_param)

    def logs(self, offset: int = 0, limit: int = 200) -> dict[str, object]:
        """Retrieve package logs.

            Parameters
            ----------
            offset : int, default=0
            limit : int, default=200

            Returns
            -------
            dict[str, object]
                Parsed response JSON into `dict`

            Example return:
            --------------
            ```python
            {
                "data" : {
                    "count" : 1,
                    "log_list" : [
                        {
                            "description_id" : 101,
                            "description_parameter" : "[\"asdf\"]",
                            "error" : 0,
                            "log_type" : 1,
                            "task_id" : 2,
                            "timestamp" : 1738341351
                        },
                    ]
                },
                "success" : True
            }
            ```
        
        """
        api_name = 'SYNO.USBCopy'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get_log_list', 'offset': offset, 'limit': limit,
                     'log_filter': '{"log_desc_id_list":[0,1,2,3,10,11,100,101,102,103,104,105,1000]}'}

        return self.request_data(api_name, api_path, req_param)

    def global_settings(self) -> dict[str, object]:
        """Retrieve package settings.

            Parameters
            ----------
            offset : int 
                (Default value = 0)
            limit : int 
                (Default value = 200)

            Returns
            -------
            dict[str, object]
                Parsed JSON into `dict`

            Example return:
            --------------
            ```python
            {
                "data" : {
                    "beep_on_task_start_end" : True,
                    "log_rotate_count" : 100000,
                    "repo_volume_path" : "/volume2"
                },
                "success" : True
            }
            ```

        """
        api_name = 'SYNO.USBCopy'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {'version': info['maxVersion'], 'method': 'get_global_setting'}

        return self.request_data(api_name, api_path, req_param)
