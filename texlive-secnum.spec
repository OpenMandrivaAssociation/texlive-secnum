%global tl_name secnum
%global tl_revision 76924

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A macro to format section numbering intuitively
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/secnum
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/secnum.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/secnum.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/secnum.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a macro \setsecnum to format section numbering
intuitively. \setsecnum{1.1.1} will set the section numbering format to
arabic.arabic.arabic and the depth to 3. The package uses LaTeX3.

