из-воздушный отоко-импорт ДАГ
из-воздушный поток.операторы.манекен импорт МанекенОператор
из датавремия импорт датавремия

default_args = {
    'владельец': 'воздушный поток',
    'ретриес': 1,
}

с ДАГ(
 dag_id='test_dag',
 default_args=default_args,
 описанье="Простой ДАГ",
 start_date=датавремия(2023, 1, 1),
 raspispisaniе_interval=Net, #Запуск вручну
 догоняукилогни,
) как даг:

 нахат = МанекенОператор(
 задача_id='нахат'
    )

 конец = МанекенОператор(
 задача_id='конец'
    )

 нахало >> конец