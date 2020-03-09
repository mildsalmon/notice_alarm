import notice_alarm
import halla
import dankook
import os
import name_list

# def run():
def start():
    univ_name = name_list.name_list_univ_name()
    notice_type = name_list.name_list_notice_type()

    choice = [univ_name[0], notice_type[0]]

    if choice[0] == univ_name[0]:
        if choice[1] == notice_type[0]:
            runner = halla.halla(univ_name[0], notice_type[0])
        elif choice[1] == notice_type[1]:
            runner = halla.halla(univ_name[0], notice_type[1])
    elif choice[0] == univ_name[1]:
        pass

    runner.web_errors(runner.req.status_code)

    if not(os.path.isfile(os.path.join(runner.BASE_DIR, runner.save_file_name))):
        runner.write_file(runner.save_boardSeq)

    chat_id = runner.show_chat_id()
    runner.matching(runner.posts, runner.use_boardSeq, chat_id)
    runner.write_file(runner.save_boardSeq)

    # self.__web_errors(req.status_code)
    # save_content, posts, user_boardSeq = self.html_analyze(req, univ_name)
    # if not(os.path.isfile(os.path.join(BASE_DIR, save_file_name))):
    #     self.write_file(BASE_DIR, save_file_name, save_content)
    # self.matching(BASE_DIR, save_file_name, posts, user_boardSeq, univ_name, bot, chat_id, notice_type)
    # self.write_file(BASE_DIR, save_file_name, save_content)