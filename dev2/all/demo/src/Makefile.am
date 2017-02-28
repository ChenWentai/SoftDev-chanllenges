lib_LTLIBRARIES = libfunc.la
libfunc_la_SOURCES = func.c func.h
libfunc_la_LDFLAGS = -version-info 1:0:0

bin_PROGRAMS = very_simple
very_simple_SOURCES = main.c
very_simple_LDADD = libfunc.la

