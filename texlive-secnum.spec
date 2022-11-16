Name:		texlive-secnum
Version:	61813
Release:	1
Summary:	A macro to format section numbering intuitively
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/secnum
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/secnum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/secnum.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/secnum.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a macro \setsecnum to format section
numbering intuitively. \setsecnum{1.1.1} will set the section
numbering format to arabic.arabic.arabic and the depth to 3.
The package uses LaTeX3.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/secnum
%{_texmfdistdir}/tex/latex/secnum
%doc %{_texmfdistdir}/doc/latex/secnum

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
