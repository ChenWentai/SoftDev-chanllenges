# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.67])
AC_INIT([project], [1], [maci@eurecom.fr])
AM_INIT_AUTOMAKE([1.9 foreign])
AC_CONFIG_SRCDIR([src/lib_foo/foo.c])
AC_CONFIG_HEADERS([config.h])

# Checks for programs.
AC_PROG_CC

# Checks for libraries.
AC_PROG_RANLIB
# Checks for header files.
AC_COMPILE_IFELSE([AC_LANG_PROGRAM([[#include <mistery.h>]],\
	 [[ mistery_value(1);]])], \
        [AC_DEFINE([MISTERY_VALUE_ONEPARAM], [], \
                [CONSTANT THAT ALLOWS TO SELECT THE RIGHT FUNCTION CALL])], \
        [AC_DEFINE([FAKE_MISTERY_VALUE_ONEPARAM], [], \
                [CONSTANT THAT ALLOWS TO SELECT THE RIGHT FUNCTION CALL])])
#       [])
# Checks for typedefs, structures, and compiler characteristics.

# Checks for library functions.
AC_SEARCH_LIBS([mistery_value], [mistery magic voodoo], [], [AC_MSG_ERROR([Libreries (mistery, magic, voodoo) not found])])

AC_CONFIG_FILES([Makefile
                 src/Makefile
                 src/lib_foo/Makefile
                 src/main/Makefile])
AC_OUTPUT

