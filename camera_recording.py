import cv2

# Параметры записи видео
video_output_filename = 'output.mp4'
frame_rate = 24  # Количество кадров в секунду
duration = 10  # Длительность записи в секундах

# Захват видео с вебкамеры
print("Запись видео...")
cap = cv2.VideoCapture(0)  # 0 - индекс вебкамеры (если у вас одна вебкамера)

# Проверка, открыта ли вебкамера
if not cap.isOpened():
    print("Не удалось открыть вебкамеру")
    exit()

# Получаем размер кадра с вебкамеры
ret, frame = cap.read()
if not ret:
    print("Не удалось захватить кадр")
    exit()
height, width, _ = frame.shape

# Создание объекта для записи видео
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(video_output_filename, fourcc, frame_rate, (width, height))

# Проверка, открыт ли файл для записи
if not out.isOpened():
    print("Не удалось открыть файл для записи")
    exit()

# Запись видео
start_time = cv2.getTickCount()
while (cv2.getTickCount() - start_time) / cv2.getTickFrequency() < duration:
    ret, frame = cap.read()
    if not ret:
        print("Не удалось захватить кадр")
        break
    out.write(frame)
    # cv2.imshow('Recording', frame)  # Показываем записываемый кадр
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Для завершения записи по нажатию 'q'
        break

# Освобождение ресурсов
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Запись видео сохранена в {video_output_filename}")