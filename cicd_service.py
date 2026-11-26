class CICDGuide:
    """Класс, формирующий данные об этапах CI/CD для курса ТИПО."""

    def __init__(self, version: str = "1.0"):
        self.version = version
        self.course_title = "Технологии внедрения программного обеспечения"
        self.stages = [
            {
                "code": "CI",
                "name": "Continuous Integration (Непрерывная интеграция)",
                "description": (
                    "Автоматическая сборка кода, проверка линтером и запуск "
                    "модульных тестов при каждом push в репозиторий."
                ),
            },
            {
                "code": "CD-1",
                "name": "Continuous Delivery (Непрерывная доставка)",
                "description": (
                    "Подготовка проверенного артефакта или Docker-образа, "
                    "готового к выкладке на сервер в один клик."
                ),
            },
            {
                "code": "CD-2",
                "name": "Continuous Deployment (Непрерывное развертывание)",
                "description": (
                    "Полностью автоматическая публикация новой версии "
                    "приложения на продуктовый сервер после успешных тестов."
                ),
            },
        ]

    def get_stages_count(self) -> int:
        return len(self.stages)

    def get_stage_by_code(self, code: str) -> dict | None:
        for stage in self.stages:
            if stage["code"].lower() == code.strip().lower():
                return stage
        return None

    def get_page_context(self) -> dict:
        return {
            "version": self.version,
            "course_title": self.course_title,
            "stages": self.stages,
            "total_stages": self.get_stages_count(),
        }
