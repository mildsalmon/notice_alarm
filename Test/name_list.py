
# 대학 이름 관련 리스트 모음
# 여러 py에서 개별적으로 관리하는 것보다
# 한 파일에서 총괄적으로 관리하는게 더 유지보수 측면에서 좋다고 생각하고
# 사실 내가 관리하기 귀찮음

def name_list_security():
    security_data_set_server_name = ["test", "halla_service", "dankook_service"]
    return security_data_set_server_name

def name_list_univ_name():
    univ_name = ["halla", "dankook"]
    return univ_name

def name_list_notice_type():
    notice_type = ["일반", "학사", "천안", "죽전", "공통"]
    return notice_type