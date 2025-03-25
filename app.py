import re, sys
from datetime import datetime, timedelta

def extract_datetime(text):
	# Define padrões para dia e horário
	day_pattern = r"(segunda|terça|quarta|quinta|sexta|sábado|domingo)"
	time_pattern = r"(\d+)\s*(da manh|da tarde|da noite|horas|hs|h|h da manha|h da tarde|h da noite)"
	time_pattern2 = r"(\d+)*(h da manha|hs da manha|h da tarde|h da noite)"

	
	# Encontrar dia e horário no texto
	day_match = re.search(day_pattern, text, re.IGNORECASE)
	time_match = re.search(time_pattern2, text, re.IGNORECASE)
	if time_match is None: time_match = re.search(time_pattern, text, re.IGNORECASE)

	if not day_match or not time_match: return None
	
	# Extrair dia e horário
	day = day_match.group(1).lower()
	time_hour = int(time_match.group(1))
	time_period = time_match.group(2).lower()
	
	# Ajustar hora com base no período
	if ("da tarde" in time_period or "da noite" in time_period) and time_hour != 12: time_hour += 12
	#elif time_period == "da noite" and time_hour != 12: time_hour += 12
	elif "da manh" in time_period and time_hour == 12: time_hour = 0
	
	# Mapear dias para dias da semana
	days_map = {
		"segunda": 0,
		"terça": 1,
		"quarta": 2,
		"quinta": 3,
		"sexta": 4,
		"sábado": 5,
		"domingo": 6
	}
	
	# Obter a data atual e calcular a data alvo
	current_date = datetime.now()
	target_weekday = days_map[day]
	
	days_ahead = target_weekday - current_date.weekday()
	if days_ahead <= 0: days_ahead += 7
	
	target_date = current_date + timedelta(days=days_ahead)
	
	# Combinar data e horário
	target_datetime = target_date.replace(hour=time_hour, minute=0, second=0, microsecond=0)
	return target_datetime

# Testar a função com a string fornecida
text = sys.argv[1]
result = extract_datetime(text)
print(result)