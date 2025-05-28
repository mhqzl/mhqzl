import logging
import allure

class AllureLogger(logging.Logger):
    formatter = None

    def __init__(self, name="AriesLogger", level="INFO", formatter=None):
        super().__init__(name)
        self.formatter = logging.Formatter(formatter)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(self.formatter)
        self.stream_handler = stream_handler
        self.addHandler(self.stream_handler)
        self.set_level(level)

    def set_level(self, level) -> None:
        self.stream_handler.setLevel(level)

    def _log(self, level, msg, args, exc_info=None, extra=None, stack_info=False,
             attached_allure='', attached_csv='', screenshots='', attached_html='',
             request_info='', response_info=''):
        sinfo = None
        try:
            fn, lno, func, sinfo = self.findCaller(stack_info)
        except ValueError:
            fn, lno, func = "(unknown file)", 0, "(unknown function)"
        record = self.makeRecord(
            self.name, level, fn, lno, msg, args, exc_info, func, extra, sinfo
        )
        title = self.formatter.format(record)
        if attached_allure or attached_csv:
            title = "*** *** {} *** ***".format(msg)
        if level >= self.stream_handler.level:
            with allure.step(title):
                if attached_allure:
                    allure.attach(
                        attached_allure,
                        "Request Details",
                        allure.attachment_type.JSON,
                    )
                if attached_csv:
                    allure.attach(
                        attached_csv,
                        "Test Details",
                        allure.attachment_type.CSV,
                    )
                if screenshots:
                    allure.attach(
                        screenshots,
                        "screenshots",
                        allure.attachment_type.PNG,
                    )
                if attached_html:
                    allure.attach(
                        attached_html,
                        "html",
                        allure.attachment_type.HTML,
                    )
                if request_info:
                    allure.attach(
                        request_info,
                        "Request Information",
                        allure.attachment_type.JSON,
                    )
                if response_info:
                    allure.attach(
                        response_info,
                        "Response Information",
                        allure.attachment_type.JSON,
                    )
        self.handle(record)

LOG_FORMATTER = "[%(asctime)s] [%(levelname)s]: %(message)s"
za_logging = AllureLogger(formatter=LOG_FORMATTER)