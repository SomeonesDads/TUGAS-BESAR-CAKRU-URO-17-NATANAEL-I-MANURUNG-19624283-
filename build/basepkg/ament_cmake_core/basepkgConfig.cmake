# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_basepkg_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED basepkg_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(basepkg_FOUND FALSE)
  elseif(NOT basepkg_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(basepkg_FOUND FALSE)
  endif()
  return()
endif()
set(_basepkg_CONFIG_INCLUDED TRUE)

# output package information
if(NOT basepkg_FIND_QUIETLY)
  message(STATUS "Found basepkg: 0.0.0 (${basepkg_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'basepkg' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${basepkg_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(basepkg_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${basepkg_DIR}/${_extra}")
endforeach()
