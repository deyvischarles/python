#!/usr/bin/env python3

import random
import math
import time

from libs.spinner import Spin

# ------------------------------------------------------------
# Função de ativação Sigmoid e sua derivada
# ------------------------------------------------------------
def sigmoid(x):
	return 1.0 / (1.0 + math.exp(-x))

def sigmoid_derivative(x):
	# x aqui é a saída da sigmoid
	return x * (1.0 - x)


# ------------------------------------------------------------
# Classe NeuralNetwork
# ------------------------------------------------------------
class NeuralNetwork:
	def __init__(self, input_size, hidden_nodes, num_outputs, learning_rate):
		# Hiperparâmetros
		self.input_size = input_size
		self.hidden_nodes = hidden_nodes
		self.num_outputs = num_outputs
		self.learning_rate = learning_rate

		# ------------------------------------------------------------
		# Inicialização dos pesos
		# Pesos da camada de entrada -> camada oculta
		# Matriz: hidden_nodes x input_size
		# ------------------------------------------------------------
		self.w1 = [[random.uniform(-1, 1) for _ in range(input_size)]
				   for _ in range(hidden_nodes)]

		# ------------------------------------------------------------
		# Pesos da camada oculta -> camada de saída
		# Matriz: num_outputs x hidden_nodes
		# ------------------------------------------------------------
		self.w2 = [[random.uniform(-1, 1) for _ in range(hidden_nodes)]
				   for _ in range(num_outputs)]

	# ------------------------------------------------------------
	# Forward propagation: calcula saídas da rede
	# ------------------------------------------------------------
	def forward(self, inputs):
		# Ativações da camada oculta
		hidden_activations = []
		for neuron_weights in self.w1:
			# soma ponderada: w * x
			s = sum(w * x for w, x in zip(neuron_weights, inputs))
			hidden_activations.append(sigmoid(s))

		# Ativações da camada de saída
		output_activations = []
		for neuron_weights in self.w2:
			s = sum(w * h for w, h in zip(neuron_weights, hidden_activations))
			output_activations.append(sigmoid(s))

		return hidden_activations, output_activations

	# ------------------------------------------------------------
	# Treinamento com Backpropagation + parada por erro mínimo
	# ------------------------------------------------------------
	def train(self, training_inputs, training_targets, epochs, target_error):
		spin = Spin("Iniciando treinamento... ")
		spin.start()
		time.sleep(1.5)

		for epoch in range(epochs):
			total_error = 0.0

			# Itera pelos exemplos de treino
			for inputs, target in zip(training_inputs, training_targets):
				
				# Forward
				hidden, outputs = self.forward(inputs)

				# ------------------------------------------------------------
				# Cálculo do erro (MSE simplificado, sem dividir por N, opcional)
				# ------------------------------------------------------------
				errors = [(t - o) for t, o in zip(target, outputs)]
				total_error += sum(e * e for e in errors)

				# ------------------------------------------------------------
				# Backpropagation na camada de saída
				# delta_output = erro * derivada(sigmoid)
				# ------------------------------------------------------------
				deltas_output = [
					e * sigmoid_derivative(o)
					for e, o in zip(errors, outputs)
				]

				# ------------------------------------------------------------
				# Backprop da camada oculta
				# delta_hidden = derivada(sigmoid) * Σ(delta_output * w)
				# ------------------------------------------------------------
				deltas_hidden = []
				for i in range(self.hidden_nodes):
					error_hidden = sum(
						deltas_output[k] * self.w2[k][i]
						for k in range(self.num_outputs)
					)
					deltas_hidden.append(error_hidden * sigmoid_derivative(hidden[i]))

				# ------------------------------------------------------------
				# Atualização dos pesos da camada oculta -> saída
				# ------------------------------------------------------------
				for k in range(self.num_outputs):
					for i in range(self.hidden_nodes):
						self.w2[k][i] += (
							self.learning_rate * deltas_output[k] * hidden[i]
						)

				# ------------------------------------------------------------
				# Atualização dos pesos da entrada -> oculta
				# ------------------------------------------------------------
				for i in range(self.hidden_nodes):
					for j in range(self.input_size):
						self.w1[i][j] += (
							self.learning_rate * deltas_hidden[i] * inputs[j]
						)

			# A cada 1000 epochs, mostra o erro
			if (epoch + 1) % 1000 == 0 or epoch == 0:
				spin.update(f"Epoca {epoch + 1}, Taxa de erro: {total_error:.4f} ")
				# time.sleep(0.1)

			# ------------------------------------------------------------
			# EARLY STOPPING – Encerrar se erro estiver abaixo do limite
			# ------------------------------------------------------------
			if total_error < target_error:
				spin.stop()
				print("-" * 60)
				print(f"Treinamento encerrado no epoch {epoch + 1}.")
				print(f"Taxa de erro: {total_error:.6f}")
				print("-" * 60)
				break

	# ------------------------------------------------------------
	# Predição
	# ------------------------------------------------------------
	def predict(self, inputs):
		spin = Spin("Processando novo dataset... ")
		spin.start()
		time.sleep(1.5)

		_, outputs = self.forward(inputs)

		spin.stop()

		return outputs


# ------------------------------------------------------------
# Exemplo de uso
# ------------------------------------------------------------
if __name__ == "__main__":
	# Problema de regressão simples com 5 inputs
	inputs = [
		[1.0, 0.5, 1.0, 1.0, 1.0],
		[0.5, 0.5, 1.0, 1.0, 1.0],
		[0.5, 1.0, 1.0, 1.0, 1.0],
		[1.0, 1.0, 1.0, 1.0, 1.0],
		[1.0, 1.0, 0.0, 1.0, 1.0],
		[1.0, 1.0, 1.0, 0.0, 0.0],
		[0.0, 1.0, 0.0, 0.0, 1.0],
		[0.0, 1.0, 0.0, 1.0, 0.0],
		[1.0, 0.5, 0.0, 0.5, 0.5],
		[0.0, 0.0, 0.0, 0.0, 0.0]
	]

	targets = [
		[1.0],
		[1.0], 
		[1.0],
		[0.8],
		[0.6],
		[0.3],
		[0.0],
		[0.0],
		[0.0],
		[0.0]
	]

	# Hiperparâmetros configuráveis
	input_size = len(inputs[0])
	hidden_nodes = 5
	num_outputs = 1
	learning_rate = 0.5
	epochs = 100000 # Máximo permitido 100.000
	target_error = 0.0001  # Erro mínimo para parar

	nn = NeuralNetwork(
		input_size = input_size,
		hidden_nodes = hidden_nodes,
		num_outputs = num_outputs,
		learning_rate = learning_rate
	)

	nn.train(inputs, targets, epochs, target_error)

	# Testes
	new_data = [
		[0.0, 0.0, 0.0, 0.0, 0.0],
		[0.0, 1.0, 0.0, 0.0, 1.0],
		[1.0, 1.0, 1.0, 0.0, 1.0],
		[1.0, 0.5, 0.5, 1.0, 0.5],
		[1.0, 0.5, 0.5, 1.0, 1.0],
		[0.0, 1.0, 1.0, 1.0, 1.0],
		[1.0, 0.5, 1.0, 1.0, 1.0]
	]

	print("\nPredição:\n")

	for sample in new_data:
		pred = nn.predict(sample)
		print(f"Entrada {sample} -> Saída {pred[0]:.1f}")

