#!/usr/bin/env python3

import sys
import time
import threading

class Spin:
	def __init__(self, msg: str = ""):
		self.template = ["⣷", "⣯", "⣟", "⡿", "⢿", "⣻", "⣽", "⣾"]
		self.msg = msg
		self._running = False
		self._thread = None
		self._lock = threading.Lock()
		
		self._last_render = ""        # último frame renderizado
		self._last_render_len = 0     # comprimento usado na linha

	def update(self, new_msg: str):
		with self._lock:
			self.msg = new_msg

	def _clear_line(self):
		sys.stdout.write("\r" + " " * self._last_render_len + "\r")
		sys.stdout.flush()

	def _spinner_loop(self):
		idx = 0
		while self._running:
			frame = self.template[idx % len(self.template)]

			with self._lock:
				msg = self.msg

			render = f"{frame} {msg}"
			new_len = len(render)

			# Apaga linha somente se o novo texto for MENOR
			if new_len < self._last_render_len:
				self._clear_line()

			# Agora renderiza normalmente
			sys.stdout.write("\r" + render)
			sys.stdout.flush()

			self._last_render_len = new_len
			self._last_render = render

			idx += 1
			time.sleep(0.1)

		# limpar apenas ao parar
		self._clear_line()

	def start(self):
		self._running = True
		self._thread = threading.Thread(target=self._spinner_loop, daemon=True)
		self._thread.start()

	def stop(self):
		if self._running:
			self._running = False
			self._thread.join()
