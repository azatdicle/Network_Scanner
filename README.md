# Ağ Tarayıcı

Bu basit Python programı, ağınızdaki cihazları taramak için kullanılabilecek bir araçtır. Kullanıcıdan IP adresi girişi alır ve sonra bu IP adresine ARP isteği göndererek ağdaki cihazları taramak için kullanır.

## Kullanım Kılavuzu

### Kurulum

Öncelikle, Python ve gerekli kütüphaneler yüklü olmalıdır. Proje dosyalarını indirin veya klonlayın.

```bash
git clone https://github.com/kullanici/adres
```

### Kullanım

Terminal veya komut istemcisini açın ve proje dizinine gidin. Ardından aşağıdaki komutu kullanarak programı çalıştırın ve hedef IP adresini belirtin.

```bash
python ağ_tarayıcı.py --ipadress <IP_ADRESI>
```

Örneğin:

```bash
python ağ_tarayıcı.py --ipadress 192.168.1.1
```

## Seçenekler

- `-i, --ipadress`: Tarama yapılacak olan IP adresini belirtir.

## Gereksinimler

- Python
- scapy kütüphanesi

## Notlar

- Bu program sadece kendi ağınızda kullanılmalıdır. Başkalarının ağına izinsiz erişim için kullanmayın.
- Programın kullanımı, ağınızı taramak için oldukça basit bir yöntem sunar. Daha karmaşık ağ tarama ve analiz ihtiyaçları için farklı araçlar ve yöntemler de bulunmaktadır.
