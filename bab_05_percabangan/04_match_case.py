# BAB 05 - match-case (membutuhkan Python 3.10 ke atas)

hari = "sabtu"

match hari:
    case "sabtu" | "minggu":
        print("Libur!")
    case "senin":
        print("Semangat!")
    case _:
        print("Hari kerja")
